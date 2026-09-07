import os

def delete_ds_store_files(txt_file_path):
    deleted_files = []

    with open(txt_file_path, 'r', encoding='utf-8') as file:
        file_paths = file.read().splitlines()

    for file_path in file_paths:
        if os.path.basename(file_path) == '.DS_Store':
            try:
                os.remove(file_path)
                deleted_files.append(file_path)
            except Exception as e:
                print(f'無法刪除檔案 {file_path}：{e}')

    return deleted_files

# 指定 .txt 檔案路徑（請使用 Unicode 編碼表示中文）
txt_file_path = r'F:\藥學相關\found_files.txt'

# 刪除 .DS_Store 檔案
deleted_files = delete_ds_store_files(txt_file_path)

# 顯示刪除的檔案位置
if deleted_files:
    print('已刪除的 .DS_Store 檔案：')
    for file_path in deleted_files:
        print(file_path)
else:
    print('未找到 .DS_Store 檔案。')
