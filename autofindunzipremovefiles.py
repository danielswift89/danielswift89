import os
import patoolib
from send2trash import send2trash  # 需要安裝 send2trash 模組

def find_zip_and_rar_files(path, output_file_path):
    zip_rar_files = []

    for root, dirs, files in os.walk(path):
        for file_name in files:
            if file_name.lower().endswith(('.zip', '.rar')):
                file_path = os.path.join(root, file_name)
                zip_rar_files.append(file_path)

    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for file_path in zip_rar_files:
            output_file.write(f'{file_path}\n')

    print(f'已將路徑輸出至：{output_file_path}')

def unzip_files_from_txt(txt_file_path, output_path):
    # 讀取 .txt 檔案
    with open(txt_file_path, 'r', encoding='utf-8') as txt_file:
        file_paths = txt_file.readlines()

    # 去除每行的換行符號並解壓縮檔案
    for file_path in file_paths:
        file_path = file_path.strip()
        file_ext = os.path.splitext(file_path)[1].lower()

        # 解壓縮 .zip、.rar 或 .7z 檔案
        if file_ext in ['.zip', '.rar', '.7z']:
            try:
                # 構建目標輸出路徑
                output_file_path = os.path.join(output_path, os.path.basename(file_path))

                # 解壓縮檔案到指定路徑
                patoolib.extract_archive(file_path, outdir=output_path)
                print(f"已解壓縮檔案：{file_path}，輸出至：{output_file_path}")

                # 移動已解壓縮的檔案至資源回收桶
                send2trash(file_path)
                print(f"已移動檔案至資源回收桶：{file_path}")
            except Exception as e:
                print(f"解壓縮檔案 '{file_path}' 時發生錯誤：{e}")

    print('已完成全部解壓縮。')

def delete_file(file_path):
    try:
        os.remove(file_path)
        print(f"已刪除檔案：{file_path}")
    except FileNotFoundError:
        print(f"找不到檔案：{file_path}")
    except PermissionError:
        print(f"無法刪除檔案：{file_path}，請檢查是否有足夠的權限。")
    except Exception as e:
        print(f"刪除檔案 '{file_path}' 時發生錯誤：{e}")

# 指定目錄路徑
directory_path = r'C:\Users\daniel\OneDrive - 嘉南藥理大學\桌面\硬碟待整理\ghost hacks 2023'

# 指定輸出的.txt檔案路徑
output_file_path = r'C:\Users\daniel\OneDrive - 嘉南藥理大學\桌面\硬碟待整理\outputfiles.txt'

# 指定輸出路徑
output_path = r'C:\Users\daniel\OneDrive - 嘉南藥理大學\桌面\硬碟待整理\ghost hacks 2023'

# 步驟1：尋找.zip和.rar檔案，並輸出至.txt檔案
find_zip_and_rar_files(directory_path, output_file_path)

# 步驟2：執行解壓縮
unzip_files_from_txt(output_file_path, output_path)

# 步驟3：逐行刪除已解壓縮的檔案
with open(output_file_path, 'r', encoding='utf-8') as txt_file:
    for line in txt_file:
        file_path = line.strip()  # 移除換行符號
        file_ext = os.path.splitext(file_path)[1].lower()

        # 只刪除 .zip、.rar 或 .7z 檔案
        if file_ext in ['.zip', '.rar', '.7z']:
            delete_file(file_path)

print('已完成全部動作。')
