import os
import shutil
import argparse

current_dir = os.getcwd()
templates_dir = os.path.join(current_dir, 'Templates')

PYTHON_TEMPLATE_PATH = os.path.join(templates_dir, 'python.py')
CPP_TEMPLATE_PATH = os.path.join(templates_dir, 'cpp.cpp')

ALLOWED = ['CodeForces', 'CodeStudio', 'LeetCode', 'GeeksForGeeks'] 
ALLOWED_EXT = ['py', 'cpp', 'java']

def copy_file(src, dest):
    try:
        shutil.copyfile(src, dest)
        print(f"File contents copied successfully from {src} to {dest}")
    except FileNotFoundError:
        print("Error: One of the specified files does not exist.")
    except PermissionError:
        print("Error: Permission denied. Make sure you have the necessary permissions.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return

def create_template_py(output) :
    try :
        copy_file(PYTHON_TEMPLATE_PATH, output)
    except Exception as e :
        print('Error occurred while copying : ', e)
    
    return

def create_template_cpp(output) :
    try :
        copy_file(CPP_TEMPLATE_PATH, output)
    except Exception as e :
        print('Error occurred while copying : ', e)
    
    return

def check_filename(fpath) :

    if(not any(x in fpath for x in ALLOWED)) :
        return False
    print('FNAME : ', fpath)
    
    _, ext = os.path.splitext(fpath)
    if(ext[1:] not in ALLOWED_EXT) :
        print('\nFNAME 123123 : ', fpath)
        return False

    return True

def main() :
    parser = argparse.ArgumentParser(description='A simple template generating tool')

    parser.add_argument('--lang', type=str, choices=['py', 'cpp'], nargs='?', default='py', help='Language')
    parser.add_argument('--file', type=str, help='Output file')

    args = parser.parse_args()

    print('ARGS : ', args)

    lang = args.lang
    f = args.file

    if(lang == 'py' and check_filename(f)) :
        create_template_py(f)

    elif(lang == 'cpp' and check_filename(f)) :
        create_template_cpp(f)

    else :
        
        return        

if __name__ == "__main__" :

    main()






 