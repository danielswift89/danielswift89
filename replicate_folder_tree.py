#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
replicate_folder_tree.py
功能：
  - 輸入：來源資料夾路徑 (src)、新空間目的地路徑 (dst)
  - 輸出：在來源資料夾生成結構紀錄檔，並在目的地複製一模一樣的資料夾編排與遞迴層數（不含檔案）。
"""

import argparse
import sys
from pathlib import Path
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description="複製資料夾的編排結構與遞迴層數到新的空間")
    parser.add_argument("src", type=str, help="來源資料夾路徑（要被複製結構的地方）")
    parser.add_argument("dst", type=str, help="新空間目的地路徑（要建立新結構的地方）")
    parser.add_argument("--dry-run", action="store_true", help="模擬執行（只生成紀錄檔並在畫面顯示預期動作，不實際建立新資料夾）")
    args = parser.parse_args()

    src_root = Path(args.src)
    dst_root = Path(args.dst)

    # 檢查來源路徑
    if not src_root.exists() or not src_root.is_dir():
        print(f"❌ 錯誤：來源路徑不存在或不是資料夾：{src_root}")
        sys.exit(1)

    print(f"🔍 開始掃描來源路徑：{src_root}")
    
    # 1. 遞迴搜尋所有子資料夾（排序好讓層數看起來由淺入深）
    subfolders = sorted([p for p in src_root.rglob('*') if p.is_dir()])

    if not subfolders:
        print("⚠️ 來源路徑下沒有找到任何子資料夾！")
        return

    print(f"✨ 成功掃描！共找到 {len(subfolders)} 個子資料夾。")

    # 2. 建立紀錄內容
    log_lines = [
        "========================================",
        "        資料夾結構備份與檢查紀錄",
        "========================================",
        f"記錄時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"來源路徑: {src_root}",
        f"目的路徑: {dst_root}",
        f"子資料夾總數: {len(subfolders)} 個",
        "----------------------------------------",
        "【收錄的相對路徑清單】:"
    ]

    for folder in subfolders:
        # 計算相對於根目錄的結構路徑
        rel_path = folder.relative_to(src_root)
        log_lines.append(f" 📂 {rel_path}")

    # 將紀錄寫入來源資料夾下的文字檔
    log_file = src_root / "collected_folders_log.txt"
    try:
        with open(log_file, "w", encoding="utf-8") as f:
            f.write("\n".join(log_lines))
        print(f"📝 結構紀錄檔已生成，你可以先去打開檢查：\n   👉 {log_file}")
    except Exception as e:
        print(f"⚠️ 無法寫入紀錄檔，錯誤：{e}")

    # 3. 在新空間建立資料夾結構
    print("\n========================================")
    print("        開始在新空間建立資料夾結構")
    print("========================================")
    
    success_count = 0
    for folder in subfolders:
        rel_path = folder.relative_to(src_root)
        # 對應到新空間的完整路徑
        target_dir = dst_root / rel_path

        if args.dry_run:
            print(f" [模擬建立] {target_dir}")
            success_count += 1
        else:
            try:
                # parents=True 會自動把上層沒建立的資料夾一起建好，exist_ok=True 遇到重複的不會報錯
                target_dir.mkdir(parents=True, exist_ok=True)
                print(f" ✅ 已建立: {target_dir}")
                success_count += 1
            except Exception as e:
                print(f" ❌ 建立失敗: {target_dir}，錯誤: {e}")

    # 執行總結
    mode_str = "【模擬】" if args.dry_run else "【實際】"
    print("\n----------------------------------------")
    print(f"🎉 執行完畢！{mode_str}成功處理 {success_count} / {len(subfolders)} 個資料夾。")
    if args.dry_run:
        print("💡 提示：目前為模擬狀態。確認無誤後，請拔掉 `--dry-run` 參數以正式建立資料夾。")

if __name__ == "__main__":
    main()