import os
from send2trash import send2trash  # 需要安裝 send2trash 模組

# 步驟1：尋找空白檔案
def find_empty_files(directory):
    empty_files = []

    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if os.path.getsize(file_path) == 0:
                empty_files.append(file_path)

    return empty_files

def export_file_paths(file_paths, output_file):
    with open(output_file, 'w', encoding='utf-8') as file:
        for path in file_paths:
            file.write(f'{path}\n')

# 指定檔案來源目錄路徑（請使用 Unicode 編碼表示中文）
source_directory = r'F:\宗翰danielPC\大學\交大'

# 尋找空白檔案
empty_files = find_empty_files(source_directory)

# 輸出檔案所在路徑至 .txt 檔案
output_file_path = os.path.join(source_directory, 'empty_files.txt')
export_file_paths(empty_files, output_file_path)
print(f'空白檔案所在路徑已輸出至：{output_file_path}')

# 步驟2：尋找空白資料夾
def find_empty_folders(directory_path, output_file_path):
    empty_folders = []

    for root, dirs, files in os.walk(directory_path, topdown=False):
        for dir_name in dirs:
            folder_path = os.path.join(root, dir_name)
            if not os.listdir(folder_path):  # 檢查資料夾是否為空
                empty_folders.append(folder_path)

    # 將空白資料夾路徑輸出到 .txt 檔案
    with open(output_file_path, 'w', encoding='utf-8') as file:
        for folder_path in empty_folders:
            file.write(folder_path + '\n')

# 指定檔案來源目錄路徑（請使用 Unicode 編碼表示中文）
source_directory = r'F:\宗翰danielPC\大學\交大'

# 指定完成輸出空白資料夾路徑的 .txt 檔案路徑
output_file_path = os.path.join(source_directory, '空白資料夾路徑.txt')

# 尋找空白資料夾並輸出路徑到 .txt 檔案
find_empty_folders(source_directory, output_file_path)

print('已完成輸出空白資料夾路徑到:', output_file_path)

# 步驟3：刪除空白檔案
def delete_empty_files(txt_file_path):
    deleted_files = []

    with open(txt_file_path, 'r', encoding='utf-8') as file:
        file_paths = file.read().splitlines()

    for file_path in file_paths:
        try:
            if os.path.getsize(file_path) == 0:
                # 移動檔案至資源回收桶
                send2trash(file_path)
                deleted_files.append(file_path)
        except Exception as e:
            print(f'無法刪除檔案 {file_path}：{e}')

    return deleted_files

# 指定 empty_files.txt 檔案路徑（請使用 Unicode 編碼表示中文）
txt_file_path = r'F:\宗翰danielPC\大學\交大\empty_files.txt'

# 刪除描述大小為 0KB 的檔案
deleted_files = delete_empty_files(txt_file_path)

# 顯示刪除的檔案位置
if deleted_files:
    print('已刪除的空白檔案：')
    for file_path in deleted_files:
        print(file_path)
else:
    print('未找到符合條件的空白檔案。')

# 步驟4：刪除空白資料夾
def delete_empty_folders(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        empty_folders = [line.strip() for line in file]

    # 遞迴刪除空白資料夾
    for folder_path in empty_folders:
        try:
            os.rmdir(folder_path)
            print('已刪除資料夾:', folder_path)
        except OSError as e:
            print('刪除資料夾失敗:', folder_path)
            print('錯誤訊息:', e)

# 指定 .txt 檔案路徑
txt_file_path = r'F:\宗翰danielPC\大學\交大\空白資料夾路徑.txt'

# 刪除空白資料夾
delete_empty_folders(txt_file_path)

print('已完成全部動作。')
