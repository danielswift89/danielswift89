import os

def create_folders_from_file(path, file_path):
    # 檢查路徑是否存在，若不存在則創建路徑
    if not os.path.exists(path):
        os.makedirs(path)
    
    # 讀取指定檔案中的名稱
    with open(file_path, 'r', encoding='utf-8') as file:
        names = file.read().splitlines()
    
    # 在指定路徑下創建資料夾
    for name in names:
        folder_path = os.path.join(path, name)
        os.makedirs(folder_path)
        print(f'已創建資料夾：{folder_path}')

# 指定路徑和檔案路徑（請使用Unicode編碼表示中文）
directory_path = r'C:\Users\daniel\OneDrive - 嘉南藥理大學\桌面\Pics'
file_path = r'C:\Users\daniel\OneDrive - 嘉南藥理大學\桌面\Pics\課表.txt'

# 呼叫函式以創建資料夾
create_folders_from_file(directory_path, file_path)
