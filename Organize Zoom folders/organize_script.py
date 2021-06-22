import shutil
import os
import datetime


def move_folder(folder_name, destination, time):
    """
    Takes in the folder name, destination and time 
    In place of time, you can pass in any folder name
    """
    try:
        os.mkdir(destination)
        print("folder created!")
    except OSError as error:
        print("Folder already exists, moving on...")

    shutil.move(folder_name + "/zoom_0.mp4", destination + "/" + time + ".mp4")


# Gather up all folder names in this directory
folder_names = []
root = './'
dirlist = [item for item in os.listdir(
    root) if os.path.isdir(os.path.join(root, item))]
for dir in dirlist:
    folder_names.append(dir)

# Move folders to new child folder, using the date as folder and time as filename
for name in folder_names:

    # Move the relevant folder (Don't try to move a folder in the correct format)
    len_name_split = len(name.split())
    if len_name_split < 2:
        continue

    old_name = name.split()
    year, month, day = [int(i) for i in old_name[0].split("-")]
    time = old_name[1]

    x = datetime.datetime(year, month, day)
    date = x.strftime("%d-%m-%Y")
    move_folder(name, date, time)

# clear old folders
for name in folder_names:
    len_name_split = len(name.split())
    if len_name_split < 2:
        continue
    shutil.rmtree(name)
