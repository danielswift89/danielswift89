import os
import unicodedata

def find_folders_with_simplified_chinese(path):
    folders_with_simplified_chinese = []

    # 遞迴遍歷目錄下的所有資料夾
    for root, dirs, _ in os.walk(path):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            # 檢查資料夾名稱是否含有簡體中文
            if contains_simplified_chinese(folder):
                folders_with_simplified_chinese.append(folder_path)

    return folders_with_simplified_chinese

def contains_simplified_chinese(text):
    for char in text:
        if 'CJK' in unicodedata.name(char, ''):
            return True
    return False

def export_to_txt(file_path, folders_list):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write("以下目錄含有簡體中文的名稱：\n")
        for folder_path in folders_list:
            file.write(folder_path + "\n")

# 指定目錄路徑（請使用 Unicode 編碼表示中文）
directory_path = r'F:\網路資源'

# 尋找含有簡體中文的資料夾
folders_with_simplified_chinese = find_folders_with_simplified_chinese(directory_path)

# 匯出結果至.txt檔案
output_file_path = os.path.join(directory_path, '含簡體中文的資料夾.txt')
export_to_txt(output_file_path, folders_with_simplified_chinese)

print(f'結果已匯出至：{output_file_path}')
