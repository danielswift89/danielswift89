import os
from collections import defaultdict

def find_duplicate_files(path):
    file_dict = defaultdict(list)

    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            file_size = os.path.getsize(file_path)
            file_type = os.path.splitext(file_name)[1]

            file_info = (file_size, file_type)
            file_dict[file_name].append(file_info + (file_path,))

    duplicate_files = {file: paths for file, paths in file_dict.items() if len(paths) > 1}

    return duplicate_files

def export_duplicates_to_txt(file_path, duplicate_files):
    with open(file_path, 'w', encoding='utf-8') as file:
        for file_name, paths in duplicate_files.items():
            file.write(f'相同檔案：{file_name}\n')
            for size, ext, path in paths:
                file.write(f'    大小：{size} 類型：{ext} 路徑：{path}\n')
            file.write('\n')

if __name__ == "__main__":
    # 指定檔案目錄路徑
    directory_path = r'F:\網路資源'

    # 尋找相同檔案
    duplicate_files = find_duplicate_files(directory_path)

    # 匯出相同檔案資訊至.txt檔案
    output_file_path = os.path.join(directory_path, 'same_file.txt')
    export_duplicates_to_txt(output_file_path, duplicate_files)
    print(f'相同檔案資訊已匯出至：{output_file_path}')
