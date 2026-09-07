import os
from opencc import OpenCC

def translate_and_rename(file_path):
    # 創建簡繁轉換器，從簡體中文轉換為繁體中文
    cc = OpenCC('s2t')

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    renamed_files = []
    not_renamed_files = []

    for line in lines:
        # 使用 opencc-python 函式庫進行簡繁轉換
        translated_name = cc.convert(line.strip())

        # 取得原始檔案路徑和檔名
        original_file_path = line.strip()
        original_file_name = os.path.basename(original_file_path)
        original_dir_path = os.path.dirname(original_file_path)

        # 取得新的檔案路徑和檔名
        new_file_name = os.path.join(original_dir_path, translated_name)
        new_file_path = os.path.join(original_dir_path, new_file_name)

        try:
            # 重新命名檔案
            os.rename(original_file_path, new_file_path)
            renamed_files.append((original_file_path, new_file_path))
        except Exception as e:
            # 若無法重新命名，則保留原檔案名稱
            not_renamed_files.append(original_file_path)

    return renamed_files, not_renamed_files

# 指定包含檔案名稱的.txt檔案路徑（請使用 Unicode 編碼表示中文）
file_path = r'F:\網路資源\輸出結果.txt'

# 翻譯檔案名稱並重新命名
renamed_files, not_renamed_files = translate_and_rename(file_path)

print("已重新命名的檔案：")
for original_path, new_path in renamed_files:
    print(f"{original_path} -> {new_path}")

print("\n未重新命名的檔案：")
for file_path in not_renamed_files:
    print(file_path)
