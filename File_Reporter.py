import os
def File_Reporter():
     """Reports Abt files in a Folder"""
     folder_search = input("Enter the folder: ")
     path = os.path.expanduser('~')
     folder_path = os.path.join(path,folder_search)
     exists = os.path.exists(folder_path)
     Dir_check = os.path.isdir(folder_path)
     if  exists == True and Dir_check == True:
          print(f"Looking for files in {folder_search}")
          New_size = 0 
          files = os.listdir(folder_path)
          for file in files:
                file_path = os.path.join(folder_path,file) 
                size = os.path.getsize(file_path) 
                MB_size = size / (1024*1024)   
                New_size += MB_size            
                print(f"Found:{file} , With size:{MB_size:.2f}")
        
          print(f"The total size is :{New_size:.2f}")
File_Reporter()
                