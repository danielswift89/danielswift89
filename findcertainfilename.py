import os

def find_files(directory, target_names):
    found_files = []

    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.lower() in target_names:
                found_files.append(os.path.join(root, file_name))

    return found_files

def export_file_paths(file_paths, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for path in file_paths:
            file.write(f'{path}\n')

# 指定檔案來源目錄路徑（請使用 Unicode 編碼表示中文）
source_directory = r'F:\藥學相關'

# 尋找目標檔案
target_names = ['.ds_store']
found_files = find_files(source_directory, target_names)

# 輸出檔案所在路徑至 .txt 檔案
output_file_path = os.path.join(source_directory, 'found_files.txt')
export_file_paths(found_files, output_file_path)
print(f'目標檔案所在路徑已輸出至：{output_file_path}')
