import os
import shutil

current_dir = os.getcwd()
root_dir = os.path.dirname(current_dir)

ALLOWED = ['CodeForces', 'CodeStudio', 'LeetCode', 'GeeksForGeeks']
ALLOWED_EXT = ['py', 'cpp', 'java']


def get_folders():
    folders = []
    for directory in os.listdir(root_dir):
        if (directory in ALLOWED):
            folders.append(directory)
    return folders


def format_resource_name(s):
    new_name = s.replace('.', '')\
                .replace(',', '')\
                .replace('_', '-')\
                .lower()

    return new_name


def ignore_dir_errors(func):

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except:
            pass

    return wrapper


@ignore_dir_errors
def refactor_to_folders(root_dir):

    try:

        for subdir in get_folders():
            subdir_path = os.path.join(root_dir, subdir)

            unique_files = {}

            for file in os.listdir(subdir_path):
                file_path = os.path.join(subdir_path, file)
                if (os.path.isdir(file_path)):
                    continue
                base_name, ext = file.split('.')
                if (ext and ext not in ALLOWED_EXT):
                    continue

                unique_files.setdefault(base_name, []).append(file_path)

            for base_name, file_paths in unique_files.items():
                unique_folder = os.path.join(subdir_path, base_name)
                if (not os.path.exists(unique_folder)):
                    os.makedirs(unique_folder, exist_ok=True)
                    for file_path in file_paths:
                        shutil.move(file_path, os.path.join(
                            unique_folder, os.path.basename(file_path)))

    except:
        pass

    return


@ignore_dir_errors
def rename_directories(root_dir):

    for dir_name in get_folders():
        dir_path = os.path.join(root_dir, dir_name)
        for subdir_name in os.listdir(dir_path):
            subdir_path = os.path.join(dir_path, subdir_name)

            new_subdir_name = format_resource_name(subdir_name)
            new_subdir_path = os.path.join(dir_path, new_subdir_name)

            if (not os.path.exists(new_subdir_path)):
                os.rename(subdir_path, new_subdir_path)
                print(f'Renamed: {subdir_name} -> {new_subdir_name}')

    return


@ignore_dir_errors
def rename_files(root_dir):

    for dir_name in get_folders():
        dir_path = os.path.join(root_dir, dir_name)
        for subdir_name in os.listdir(dir_path):
            subdir_path = os.path.join(dir_path, subdir_name)
            if (os.path.isdir(subdir_path)):
                for f in os.listdir(subdir_path):
                    file_name, ext = f.split('.')
                    if (ext not in ALLOWED_EXT):
                        continue
                    new_file_name = '{}.{}'.format('main', ext)

                    file_path = os.path.join(subdir_path, f)
                    new_file_path = os.path.join(subdir_path, new_file_name)

                    if (not os.path.exists(new_file_path)):
                        os.rename(file_path, new_file_path)
                        print(f'Renamed: {file_name} -> {new_file_name}')

    return


if __name__ == '__main__':

    refactor_to_folders(root_dir)
    rename_directories(root_dir)
    rename_files(root_dir)
