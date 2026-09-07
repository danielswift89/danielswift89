import os
from googletrans import Translator

# 初始化 Google 翻譯器
translator = Translator()

def translate_and_rename_files(directory):
    for root, dirs, files in os.walk(directory):
        for file_name in files:
            # 檔案的完整路徑
            file_path = os.path.join(root, file_name)
            
            # 取得原始檔案名稱 (不包含路徑)
            original_file_name = os.path.basename(file_path)
            
            # 取得檔案名稱部分 (不包含副檔名)
            base_name, extension = os.path.splitext(original_file_name)
            
            # 翻譯檔案名稱
            translated_name = translator.translate(base_name, src='en', dest='zh-TW').text
            
            # 重新命名檔案
            new_file_name = f'{translated_name}{extension}'
            new_file_path = os.path.join(root, new_file_name)
            os.rename(file_path, new_file_path)
            
            # 顯示原名稱及翻譯後的名稱
            print(f'原名稱：{original_file_name}，翻譯名稱：{new_file_name}')

# 指定目錄路徑（請使用 Unicode 編碼表示中文）
directory_path = r'F:\宗翰danielPC\同捆包風暴'

# 呼叫函式執行翻譯及重新命名
translate_and_rename_files(directory_path)
