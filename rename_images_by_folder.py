#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
rename_images_by_folder.py
功能：
  - 輸入：一個資料夾路徑（root）
  - 輸出：將 root 底下每個子資料夾內的圖片檔（png/jpg/jpeg/...）
         依子資料夾名稱重新命名為 FolderName(1).jpg, FolderName(2).jpg, ...
備註：
  - 預設不會覆寫已存在檔案（可用 --overwrite 開啟）。
  - 建議先使用 --dry-run 測試。
依賴：Pillow (pip install pillow)
"""

import argparse
import sys
from pathlib import Path
import shutil
import logging
from datetime import datetime

try:
    from PIL import Image, ImageOps
except ImportError:
    print("錯誤：需要安裝 Pillow。請執行：pip install pillow")
    sys.exit(1)

# 可接受之影像副檔名（小寫）
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.webp', '.gif'}

def is_image_file(p: Path) -> bool:
    return p.is_file() and p.suffix.lower() in IMAGE_EXTS

def safe_mkdir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def convert_to_jpeg(src: Path, dst: Path):
    """
    開啟 src，處理 EXIF 方向、透明度，並儲存成 JPEG 到 dst。
    若為動畫 GIF，僅儲存第一張影格（會有資料限制）。
    """
    with Image.open(src) as im:
        # 修正 exif orientation
        im = ImageOps.exif_transpose(im)

        # 若為有 alpha 的模式，合成白底
        if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
            rgba = im.convert('RGBA')
            background = Image.new('RGB', rgba.size, (255, 255, 255))
            # alpha channel paste
            background.paste(rgba, mask=rgba.split()[-1])
            background.save(dst, format='JPEG', quality=95)
        else:
            rgb = im.convert('RGB')
            rgb.save(dst, format='JPEG', quality=95)

def process_one_folder(folder: Path, dry_run=False, backup=False, overwrite=False, start_index=1):
    """
    處理單一子資料夾：將該資料夾內所有影像依排序轉成並命名為 FolderName(n).jpg
    回傳 summary dict
    """
    summary = {'folder': str(folder), 'found': 0, 'renamed': 0, 'errors': 0, 'skipped': 0}
    # 搜尋影像檔（非遞迴）
    images = sorted([p for p in folder.iterdir() if is_image_file(p)])
    summary['found'] = len(images)

    if summary['found'] == 0:
        return summary

    # 若需備份，建立備份資料夾（時間戳避免衝突）
    backup_dir = None
    if backup:
        stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_dir = folder / f"_backup_originals_{stamp}"
        safe_mkdir(backup_dir)
        if dry_run:
            print(f"[DRY RUN] 會備份 {len(images)} 個檔案到 {backup_dir}")
        else:
            for p in images:
                shutil.copy2(p, backup_dir / p.name)

    idx = start_index
    for p in images:
        try:
            # 生成下一個可用的 target path（避免覆寫）
            target = folder / f"{folder.name}({idx}).jpg"
            while target.exists() and not overwrite:
                idx += 1
                target = folder / f"{folder.name}({idx}).jpg"

            # 若 dry-run，僅顯示預期動作
            if dry_run:
                print(f"[DRY RUN] {p.name} -> {target.name}")
                idx += 1
                continue

            # 若原本就是 jpg/jpeg，且檔案本身不需要內容轉換，可以直接改名（效率高）
            src_suffix = p.suffix.lower()
            if src_suffix in ('.jpg', '.jpeg'):
                # 直接 rename（若 target 與 p 為同一路徑但名稱不同，使用 rename）
                # 若 target 與 p 相同檔名，則跳過
                if p.resolve() == target.resolve():
                    summary['skipped'] += 1
                else:
                    # 若 overwrite 為 True，先移除 target（避免 rename 失敗）
                    if target.exists() and overwrite:
                        target.unlink()
                    p.rename(target)
                    summary['renamed'] += 1
            else:
                # 需要格式轉換（例如 png -> jpg）
                convert_to_jpeg(p, target)
                # 轉換成功後，移除原始檔（因為我們已完成「改名/轉檔」）
                p.unlink()
                summary['renamed'] += 1

            idx += 1

        except Exception as e:
            summary['errors'] += 1
            logging.exception(f"處理檔案失敗：{p}，錯誤：{e}")

    return summary

def find_subfolders(root: Path, recursive=False):
    if recursive:
        return [p for p in root.rglob('*') if p.is_dir()]
    else:
        return [p for p in root.iterdir() if p.is_dir()]

def main():
    parser = argparse.ArgumentParser(description="將每個子資料夾內的圖片重新命名為 FolderName(1).jpg, FolderName(2).jpg ...")
    parser.add_argument("root", type=str, help="欲處理的根資料夾路徑")
    parser.add_argument("--dry-run", action="store_true", help="模擬執行（不實際修改檔案）")
    parser.add_argument("--backup", action="store_true", help="先備份原始檔案到子資料夾 _backup_originals_TIMESTAMP")
    parser.add_argument("--recursive", action="store_true", help="遞迴處理所有子資料夾（預設僅處理第一層子資料夾）")
    parser.add_argument("--overwrite", action="store_true", help="若目標檔名已存在則覆寫（危險）")
    parser.add_argument("--start-index", type=int, default=1, help="從第幾號開始編號（預設 1）")
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists() or not root.is_dir():
        print(f"錯誤：路徑不存在或不是資料夾：{root}")
        sys.exit(1)

    subfolders = find_subfolders(root, recursive=args.recursive)
    if not subfolders:
        print("找不到任何子資料夾。請確認路徑或是否需要 --recursive。")
        return

    # 記錄所有處理到的資料夾名稱
    record_lines = []
    overall = {'folders': 0, 'images_found': 0, 'renamed': 0, 'errors': 0, 'skipped': 0}

    for folder in subfolders:
        print(f"處理資料夾：{folder}")
        summary = process_one_folder(folder, dry_run=args.dry_run, backup=args.backup, overwrite=args.overwrite, start_index=args.start_index)
        record_lines.append(f"{folder.name}: found={summary['found']}, renamed={summary['renamed']}, skipped={summary['skipped']}, errors={summary['errors']}")
        overall['folders'] += 1
        overall['images_found'] += summary['found']
        overall['renamed'] += summary['renamed']
        overall['errors'] += summary['errors']
        overall['skipped'] += summary['skipped']

    # 將 record 寫到 root 下的檔案
    record_file = root / "processed_folders_record.txt"
    if args.dry_run:
        print(f"[DRY RUN] 會建立記錄檔：{record_file}")
    else:
        with open(record_file, 'w', encoding='utf-8') as f:
            f.write("Processed folders summary\n")
            f.write(f"Root: {root}\n")
            f.write(f"Timestamp: {datetime.now().isoformat()}\n\n")
            for line in record_lines:
                f.write(line + "\n")
            f.write("\nOverall:\n")
            f.write(str(overall) + "\n")
        print(f"完成。已建立記錄檔：{record_file}")

    # 顯示總結
    print("執行摘要：")
    print(overall)

if __name__ == "__main__":
    main()
