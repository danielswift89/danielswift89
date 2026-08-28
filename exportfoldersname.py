import os

def get_folder_names(path):
    folder_names = []
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            folder_names.append(dir_name)
    return folder_names

def save_folder_names_to_txt(file_path, folder_names):
    with open(file_path, 'w', encoding='utf-8') as file:
        for folder_name in folder_names:
            file.write(f"{folder_name}\n")

# 指定路徑（請使用Unicode編碼表示中文）
directory_path = r'C:\Users\daniel\OneDrive - 嘉南藥理大學\桌面\0528更新檔案'

# 取得所有資料夾名稱
all_folder_names = get_folder_names(directory_path)

# 儲存資料夾名稱至.txt檔案
output_file_path = os.path.join(directory_path, '所有資料夾名稱.txt')
save_folder_names_to_txt(output_file_path, all_folder_names)
print(f"所有資料夾名稱已儲存至：{output_file_path}")
