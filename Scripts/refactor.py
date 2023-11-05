import os
import shutil

current_dir = os.getcwd()
root_dir = os.path.dirname(current_dir)
print('current dir : ', current_dir)
print('root dir : ', root_dir)

ALLOWED = ['CodeForces', 'CodeStudio', 'LeetCode', 'GeeksForGeeks'] 

def get_folders() :
    folders = []
    for directory in os.listdir(root_dir) :
        if(directory in ALLOWED) :
            folders.append(directory) 
    return folders


def format_resource_name(s, prefix) :
    new_name = s.replace(prefix, '')\
                .replace('.', '')\
                .replace(',', '')\
                .replace('_', '-')\
                .lower()
    
    return new_name

def refactor_to_folders(root_dir) :

    for subdir in get_folders() :
        subdir_path = os.path.join(root_dir, subdir)
        
        unique_files = {}

        for file in os.listdir(subdir_path):
            file_path = os.path.join(subdir_path, file)
            base_name = os.path.splitext(file)[0]

            unique_files.setdefault(base_name, []).append(file_path)

        for base_name, file_paths in unique_files.items():
            unique_folder = os.path.join(subdir_path, base_name)
            if(os.path.exists(unique_folder)) :
                # print(f'Skipping : {unique_folder} already exists')
            else :
                os.makedirs(unique_folder, exist_ok=True)
                for file_path in file_paths:
                    shutil.move(file_path, os.path.join(unique_folder, os.path.basename(file_path)))

                    print(f'Moved {base_name} to {unique_folder}')
    return

def rename_directories(root_dir):

    for dir_name in get_folders():
        prefix = dir_name + '_'
        dir_path = os.path.join(root_dir, dir_name)
        for subdir_name in os.listdir(dir_path) :
            subdir_path = os.path.join(dir_path, subdir_name)
            
            new_subdir_name = format_resource_name(subdir_name, prefix)
            new_subdir_path = os.path.join(dir_path, new_subdir_name)
            
            if(os.path.exists(new_subdir_path)) :
                # print(f'Skipping : {new_subdir_name} already exists')
            else :
                os.rename(subdir_path, new_subdir_path)
                print(f'Renamed: {subdir_name} -> {new_subdir_name}')
    
    return
            

def rename_files(root_dir) :

    for dir_name in get_folders():
        dir_path = os.path.join(root_dir, dir_name)
        for subdir_name in os.listdir(dir_path) :
            subdir_path = os.path.join(dir_path, subdir_name)
            for f in os.listdir(subdir_path) :
                file_name, ext = f.split('.')
                new_file_name = '{}.{}'.format('main', ext)

                file_path = os.path.join(subdir_path, f)
                new_file_path = os.path.join(subdir_path, new_file_name)
                
                if(os.path.exists(new_file_path)) :
                    # print(f'Skipping : {file_name} already exists')
                else :
                    os.rename(file_path, new_file_path)
                    print(f'Renamed: {file_name} -> {new_file_name}')

    return
            

if __name__ == '__main__' :
   
    refactor_to_folders(root_dir)
    rename_directories(root_dir)
    rename_files(root_dir)