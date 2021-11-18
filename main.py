## Run these in terminal or CMD
# pip install patool pyunpack
# pip install prettytable

#import zipfile
import os
import time
from pyunpack import Archive
from prettytable import PrettyTable
from prettytable import MARKDOWN

path_to_zip_file = input("enter directory:")
listdir = os.listdir(path_to_zip_file)
zip_files = []
files_to_unzip = []
folder_names = []

for ls in listdir:
    if ls.endswith(".zip") or ls.endswith(".rar"):
        zip_files.append(ls)
for files in zip_files:
    files_to_unzip.append(f"{path_to_zip_file}/{files}")
    folder_names.append(files[:-4])
for files in folder_names:
    path_to_extract_to = f"{path_to_zip_file}/{files}"
    os.makedirs(path_to_extract_to, exist_ok=True)

i = 1
myTable = PrettyTable(["#", "Name", "Status", "Time", "File size"])
for file in files_to_unzip:
    start = time.time()
    path_to_extract_to = f"{file[:-4]}"
    # size = os.path.getsize(file)
    final_size = "{:.3f}".format(os.path.getsize(file) / 1024 / 1000)
    print(f"Job {i} in progress - File size: {final_size} Mb.")

    Archive(file).extractall(path_to_extract_to)
    stop = time.time()
    duration = "{:.3f}".format(stop-start)
    file_name = str(file.rsplit("/", 1)[1])
    file_name = f"{file_name[:]}"
    myTable.add_row([i, file_name, "Unpacked", f"{duration} s", f"{final_size} Mb"])
    print(f"Job {i} done in {duration}s \n {'-'*10}")
    i += 1

myTable.align = "l"
myTable.align["Name"] = "c"
myTable.set_style(MARKDOWN)
print("Everything done, enjoy")
print("\n")
print("Results: \n", myTable)
