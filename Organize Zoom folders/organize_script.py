import shutil, os

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

    shutil.move(folder_name + "/zoom_0.mp4", destination +  "/" + time + ".mp4")

# Gather up all folder names in this directory
folder_names = []
root='./'
dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
for dir in dirlist:
    folder_names.append(dir)

# Move folders to new child folder, using the date as folder and time as filename
for name in folder_names:
    old_name = name.split()
    date = old_name[0]
    time = old_name[1]

    move_folder(name, date, time)

# clear old folders
for name in folder_names:
    shutil.rmtree(name)

