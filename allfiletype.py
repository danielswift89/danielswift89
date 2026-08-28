import os
from collections import defaultdict

def find_files_by_type(path):
    file_types = defaultdict(list)

    # 遞迴遍歷目錄下的所有檔案
    for root, _, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_extension = os.path.splitext(file_name)[1].lower()  # 取得檔案副檔名

            # 將檔案類型及其所在目錄加入字典
            file_types[file_extension].append(file_path)

    return file_types

def export_to_txt(file_path, file_types):
    with open(file_path, 'w', encoding='utf-8') as file:
        for file_type, file_paths in file_types.items():
            file.write(f'檔案類型：{file_type}\n')
            file.write(f'檔案所在目錄：\n')
            for path in file_paths:
                file.write(f'{path}\n')
            file.write('\n')

# 指定目錄路徑（請使用 Unicode 編碼表示中文）
directory_path = r'F:\網路資源'

# 尋找檔案類型及其所在的目錄
file_types = find_files_by_type(directory_path)

# 將結果輸出到 .txt 檔案
output_file_path = os.path.join(directory_path, '檔案類型結果.txt')
export_to_txt(output_file_path, file_types)

print(f'檔案類型結果已匯出至：{output_file_path}')
