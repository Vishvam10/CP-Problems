import os
import shutil
import argparse

NOT_ALLOWED = ['.git', 'README.md', 'Scripts', 'Topics'] 

class CLI :
    def __init__(self) :
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description='Parameters for commit message', allow_abbrev=True, add_help=True)
        
        self.parser.add_argument('-fr', help='Force rename', action='store_true')
        self.parser.add_argument('-fo', help='Force overwrite', action='store_true')
        self.parser.add_argument('-d', help='Default Settings', action='store_false')
    
    def get_args(self) :
        return self.parser.parse_args()

def rename_files(folder, extension, force_rename, force_overwrite) :
    affected_files = []
    for directory in os.listdir(os.path.abspath('../')) :
        abs_path = '../{}'.format(directory)
        if(directory not in NOT_ALLOWED and directory == folder and os.path.isdir(abs_path)) :
            for file in os.listdir(abs_path):
                if(not file.startswith(folder)) :
                    formatted_name = standard_format(file).split('.')[0]
                    new_name = '{}_{}.{}'.format(folder, formatted_name, extension)
                    affected_files.append({
                        'old_file_name' : file,
                        'new_file_name' : new_name,
                        'old_file_path': os.path.join(abs_path, file), 
                        'new_file_path': os.path.join(abs_path, new_name)
                    })
    
    print('\n***************** FILES AFFECTED ***************** \n')
    for i in range(len(affected_files)) :
        print(affected_files[i].get('old_file_name'), ' ---> ', affected_files[i]['new_file_name'])
    print('\n***************************************************\n')

    old_file_path = affected_files[i].get('old_file_path')
    new_file_path = affected_files[i].get('new_file_path')
    
    if(not force_rename) :
        inp = input('Accept changes ? (y/n) ')
        if(inp.strip() == 'y') :
            if(force_overwrite) :
                for i in range(len(affected_files)) :
                    try:
                        shutil.copy2(old_file_path, new_file_path)
                        print('File {} overwritten.'.format(new_file_path))
                        try:
                            os.remove(old_file_path)
                        except OSError as e:
                            print(f'Error deleting old file: {e}')
                    except Exception as e:
                        print('Skipping {} as an error occurred: {}'.format(new_file_path, str(e)))
            else :      
                for i in range(len(affected_files)) :
                    try :
                        os.rename(old_file_path, new_file_path)
                    except :
                        msg = 'Skipping {} as it already exists.'.format(new_file_path)
                        print(msg)
                        pass
        else :
            return
    else :

        for i in range(len(affected_files)) :
            try :
                os.rename(old_file_path, new_file_path)
            except :
                msg = 'Skipping {} as it already exists.'.format(new_file_path)
                print(msg)
                pass
        return

def standard_format(s) :
    return s.replace(' ', '_')\
            .replace('-', '_')\
            .replace(',', '')\
            .lower()

def RenameDirectory(folder_name='LeetCode', extension='py', force_rename=False, force_overwrite=False) :
    rename_files(folder_name, extension, force_rename, force_overwrite)

if __name__ == '__main__' :
    cli = CLI().get_args()
    force_rename = cli.fr
    force_overwrite = cli.fo
    default_settings = cli.d
    print('\nrename : ', force_rename)
    print('overwrite : ', force_overwrite)
    if(default_settings) :
        folder_name = 'LeetCode'
        extension = 'py'
        RenameDirectory(folder_name, extension, force_rename, force_overwrite)
    else :
        
        folders = [f for f in os.listdir(os.path.abspath('../')) if f not in NOT_ALLOWED]
        print()
        for i, f in enumerate(folders) :
            msg = '{}) {}'.format(i, f)
            print(msg)
        
        try :
            folder_ind = int(input('\nChoose the folder (0-{}) : '.format(len(folders)-1)).strip())
        except :
            print('\nInvalid number !')
            exit(0)
        if(folder_ind > len(folders) or folder_ind < 0) :
            print('\nInvalid number !')
            exit(0)

        chosen_folder = folders[folder_ind]
        print('\nChosen folder : ', chosen_folder)
        # extension = input('\nEnter the extension with dot (.) : ').strip()
        RenameDirectory(folder_name=chosen_folder, extension='.py', force_rename=force_rename, force_overwrite=force_overwrite)
        
