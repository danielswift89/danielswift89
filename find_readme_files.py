import os

def find_readme_files(directory):
    readme_files = []

    for root, _, files in os.walk(directory):
        for file_name in files:
            if file_name.lower() == 'readme.txt' or file_name == '自述文件.txt':
                readme_files.append(os.path.join(root, file_name))

    return readme_files

def export_readme_paths(readme_paths, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for path in readme_paths:
            file.write(f'{path}\n')

# 指定檔案來源目錄路徑（請使用 Unicode 編碼表示中文）
source_directory = r'F:'

# 尋找自述文件
readme_files = find_readme_files(source_directory)

# 輸出自述文件所在路徑至 .txt 檔案
output_file_path = os.path.join(source_directory, 'readme_paths.txt')
export_readme_paths(readme_files, output_file_path)
print(f'自述文件所在路徑已輸出至：{output_file_path}')
