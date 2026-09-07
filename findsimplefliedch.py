import os
import re

def contains_simplified_chinese(text):
    # 利用正規表達式判斷檔案名稱是否包含簡體中文
    chinese_pattern = re.compile(r'[\u4e00-\u9fff]')
    return chinese_pattern.search(text) is not None

def find_files_with_simplified_chinese(directory_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        # 遞迴遍歷目錄下的所有檔案
        for root, dirs, files in os.walk(directory_path):
            for file_name in files:
                # 檢查檔案名稱是否包含簡體中文
                if contains_simplified_chinese(file_name):
                    file_path = os.path.join(root, file_name)
                    output_file.write(file_path + '\n')

# 指定目錄路徑（請使用 Unicode 編碼表示中文）
directory_path = r'F:\藥學相關'

# 指定輸出的 .txt 檔案路徑
output_file_path = r'F:\藥學相關\輸出結果.txt'

# 尋找包含簡體中文的檔案並將路徑寫入 .txt 檔案
find_files_with_simplified_chinese(directory_path, output_file_path)
print(f'包含簡體中文的檔案路徑已輸出至：{output_file_path}')
