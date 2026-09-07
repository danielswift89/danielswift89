import os
import unicodedata
from googletrans import Translator

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

def translate_to_traditional_chinese(text):
    translator = Translator()
    return translator.translate(text, src='zh-CN', dest='zh-TW').text

def rename_folders_recursive(path):
    # 尋找含有簡體中文的資料夾
    folders_with_simplified_chinese = find_folders_with_simplified_chinese(path)

    # 先處理最底層的資料夾
    for folder_path in folders_with_simplified_chinese:
        folder_name = os.path.basename(folder_path)
        translated_name = translate_to_traditional_chinese(folder_name)
        new_folder_path = os.path.join(os.path.dirname(folder_path), translated_name)

        # 重命名資料夾
        os.rename(folder_path, new_folder_path)

    # 繼續遞迴處理上層資料夾
    for root, dirs, _ in os.walk(path, topdown=False):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            if folder_path in folders_with_simplified_chinese:
                # 已處理過的資料夾跳過
                continue
            folder_name = os.path.basename(folder_path)
            translated_name = translate_to_traditional_chinese(folder_name)
            new_folder_path = os.path.join(os.path.dirname(folder_path), translated_name)

            # 重命名資料夾
            os.rename(folder_path, new_folder_path)

if __name__ == "__main__":
    # 指定目錄路徑（請使用 Unicode 編碼表示中文）
    directory_path = r'F:\網路資源'

    # 開始遞迴處理資料夾
    rename_folders_recursive(directory_path)

    print("資料夾翻譯並重新命名完成。")
