#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
remove_empty_folders.py
功能：
  - 掃描指定路徑底下的所有子資料夾（遞迴到最底層）。
  - 找出完全空白的資料夾並記錄列出。
  - 等待使用者輸入 'delete' 後，一次性將這些空資料夾刪除。
"""

import argparse
import sys
from pathlib import Path

def get_empty_dirs(root_path: Path):
    empty_dirs = []
    
    # 抓出所有子資料夾，並依據路徑層數「由深到淺」排序
    # 這樣如果有多層空殼資料夾 (例如 A/B 裡面都是空的)，可以更清楚地列出來
    all_dirs = sorted(
        [p for p in root_path.rglob('*') if p.is_dir()],
        key=lambda p: len(p.parts),
        reverse=True
    )

    for d in all_dirs:
        try:
            # 檢查資料夾內是否有任何檔案或子資料夾
            if not any(d.iterdir()):
                empty_dirs.append(d)
        except PermissionError:
            print(f"⚠️ 權限不足，略過檢查：{d}")
            
    return empty_dirs

def main():
    parser = argparse.ArgumentParser(description="找出並一次性刪除所有空白資料夾")
    parser.add_argument("target_path", type=str, help="欲掃描的目標資料夾路徑")
    args = parser.parse_args()

    root = Path(args.target_path)

    if not root.exists() or not root.is_dir():
        print(f"❌ 錯誤：找不到此路徑或它不是一個資料夾：{root}")
        sys.exit(1)

    print(f"🔍 開始掃描：{root}")
    empty_folders = get_empty_dirs(root)

    if not empty_folders:
        print("✨ 太棒了！這個路徑底下沒有任何空白資料夾。")
        return

    # 列出所有找到的空資料夾
    print("\n========================================")
    print(f"      找到 {len(empty_folders)} 個空白資料夾")
    print("========================================")
    for folder in empty_folders:
        print(f" 📂 {folder}")
    print("----------------------------------------\n")

    # 要求使用者輸入指令
    user_input = input("⚠️ 請檢查上方清單。若要全部刪除，請輸入 'delete' (輸入其他任意內容則取消)：")

    if user_input.strip() == "delete":
        print("\n🗑️ 開始刪除作業...")
        success_count = 0
        for folder in empty_folders:
            try:
                folder.rmdir()
                print(f" ✅ 已刪除: {folder}")
                success_count += 1
            except Exception as e:
                print(f" ❌ 刪除失敗: {folder}，原因: {e}")
                
        print(f"\n🎉 執行完畢！成功刪除 {success_count} / {len(empty_folders)} 個空白資料夾。")
    else:
        print("\n🚫 已取消刪除作業，你的資料夾毫髮無傷！")

if __name__ == "__main__":
    main()