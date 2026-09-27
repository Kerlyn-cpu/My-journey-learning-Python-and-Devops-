import os 
import shutil

def Backup_Tool():
    home_path = os.path.expanduser('~')
    source_name = input("Enter the folder to back up: ")
    folder_path = os.path.join(home_path,source_name)
    folder_exists = os.path.exists(folder_path)
    folder_check = os.path.isdir(folder_path)
    if folder_exists == True and folder_check == True:
         Target_name= input ("Enter the target location: ")
         Target_location = os.path.join(home_path,Target_name)
         shutil.copytree(folder_path,Target_location)
         print("Done😌")
Backup_Tool()    