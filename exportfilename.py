import os

def list_files(directory):
    file_list = []
    for entry in os.scandir(directory):
        if entry.is_file():
            # 移除不需要的字元
            file_name = entry.name.replace(r'C:\Users\daniel\OneDrive - 嘉南藥理大學\桌面\Samsung notes\病態生理學\期末\', '')
            file_list.append(file_name)
    return file_list

def write_to_txt(file_list, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for file in file_list:
            f.write(file + '\n')

# 指定目錄路徑
directory_path = r'C:\Users\daniel\OneDrive - 嘉南藥理大學\桌面\Samsung notes\病態生理學\期末'

# 指定輸出檔案路徑和名稱
output_file_path = r'C:\Users\daniel\OneDrive - 嘉南藥理大學\桌面\Samsung notes\病態生理學\期末\filenames.txt'

# 取得指定目錄下的所有檔案列表
files = list_files(directory_path)

# 將檔案列表寫入到指定的.txt檔案中
write_to_txt(files, output_file_path)

print('檔案名稱已匯入到指定路徑的.txt檔案中。')

