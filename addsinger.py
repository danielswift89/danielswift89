import os

def add_prefix_to_files(path, prefix_string):
    # 獲取目標目錄下的所有檔案名稱
    files = os.listdir(path)
    
    for file_name in files:
        if not file_name.startswith(prefix_string):
            # 添加指定前綴字串後重新命名檔案
            new_file_name = prefix_string + file_name
            
            # 使用 os.rename 函式重新命名檔案
            old_file_path = os.path.join(path, file_name)
            new_file_path = os.path.join(path, new_file_name)
            os.rename(old_file_path, new_file_path)
            
            print(f'已重新命名檔案：{file_name} -> {new_file_name}')

# 指定目錄路徑（請使用 Unicode 編碼表示中文）
directory_path = r'C:\Users\daniel\Music\英文歌(2023.7.27)\Taylor Swift\Fearless'

# 指定要添加的前綴字串
prefix_string = 'Taylor Swift - '

# 呼叫函式重新命名符合條件的檔案
add_prefix_to_files(directory_path, prefix_string)

