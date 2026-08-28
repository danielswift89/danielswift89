import os
from collections import defaultdict

def find_duplicate_files_with_max_size(path):
    file_dict = defaultdict(list)

    # 遞迴遍歷目錄下的所有檔案
    for root, dirs, files in os.walk(path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # 只考慮檔案名稱相同的檔案
            file_dict[file_name].append(file_path)

    # 找出檔案名稱相同且大小相同的重複檔案，但保留其中一個
    for file_name, paths in file_dict.items():
        unique_files = set()  # 用來儲存不重複的檔案路徑

        for file_path in paths:
            file_size = os.path.getsize(file_path)
            file_info = (file_path, file_size)

            if file_info in unique_files:
                # 如果檔案大小和路徑已經出現過，代表是重複的相同大小檔案
                # 刪除這個檔案
                os.remove(file_path)
            else:
                unique_files.add(file_info)

# 指定目錄路徑（請使用 Unicode 編碼表示中文）
directory_path = r'F:\宗翰danielPC'

# 尋找重複檔案並保留其中一個檔案，刪除其他重複的相同大小檔案
find_duplicate_files_with_max_size(directory_path)
