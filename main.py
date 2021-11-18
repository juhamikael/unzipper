import zipfile
import os
import time
from pyunpack import Archive

path_to_zip_file = "E:/1 Downloads 2021 - 2022/New I Don't Wanna Be Right Vox Stems/New folder/New folder"
listdir = os.listdir(path_to_zip_file)
zip_files = []
for ls in listdir:
    # print(ls)
    if ls.endswith(".zip") or ls.endswith(".rar"):
        zip_files.append(ls)

files_to_unzip = []
folder_names = []
for files in zip_files:
    files_to_unzip.append(f"{path_to_zip_file}/{files}")
    folder_names.append(files[:-4])

for files in folder_names:
    path_to_extract_to = f"{path_to_zip_file}/{files}"
    os.makedirs(path_to_extract_to, exist_ok=True)
i = 1
for file in files_to_unzip:
    start = time.time()
    path_to_extract_to = f"{file[:-4]}"
    Archive(file).extractall(path_to_extract_to)
    stop = time.time()
    duration = stop-start
    format_duration = "{:.3f}".format(duration)
    print(f"{i}. ZipFile - unpacked. It took {format_duration} seconds!")
    i += 1
print("Job done, enjoy")
