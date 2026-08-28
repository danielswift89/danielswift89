import os

def rename_files_with_string(path, target_string):
    # 獲取目標目錄下的所有檔案名稱
    files = os.listdir(path)
    
    for file_name in files:
        if target_string in file_name:
            # 刪除目標字串後重新命名檔案
            new_file_name = file_name.replace(target_string, '')
            
            # 使用 os.rename 函式重新命名檔案
            old_file_path = os.path.join(path, file_name)
            new_file_path = os.path.join(path, new_file_name)
            os.rename(old_file_path, new_file_path)
            
            print(f'已重新命名檔案：{file_name} -> {new_file_name}')

# 指定目錄路徑（請使用 Unicode 編碼表示中文）
directory_path = r'/指定的目錄路徑'

# 指定要刪除的目標字串
target_string = '(Official Audio)'

# 呼叫函式重新命名符合條件的檔案
rename_files_with_string(directory_path, target_string)
