import os
import subprocess
import shutil
import argparse

current_dir = os.getcwd()
root_dir = os.path.dirname(current_dir)
templates_dir = os.path.join(root_dir, "Templates")

PYTHON_TEMPLATE_PATH = os.path.join(templates_dir, "python.py")
CPP_TEMPLATE_PATH = os.path.join(templates_dir, "cpp.cpp")

ALLOWED = {
    "cf": "CodeForces",
    "cs": "CodeStudio",
    "lc": "LeetCode",
    "gfg": "GeeksForGeeks",
    "cses": "CSES",
}

ALLOWED_EXT = ["py", "cpp", "go", "rs"]


def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
        print("File contents copied successfully !")
    except Exception as e:
        print(f"An error occurred: {e}")
    return


def create_template(cstr):
    platform, problem, language = cstr.split("/")
    folder = ALLOWED[platform]
    fpath = os.path.join(root_dir, folder, problem)
    fname = f"main.{language}"

    file_path = os.path.join(fpath, fname)

    if not os.path.exists(fpath):
        try:
            os.makedirs(fpath)
            with open(file_path, "w"):
                pass
        except OSError as e:
            print(f"Error while creating file : {e}")
    else:
        print("Folder already exists : ", fpath)
        files = [f for f in os.listdir(fpath) if os.path.isfile(os.path.join(fpath, f))]

        if fname in files:
            return

    if language == "py":
        create_template_py(file_path)
    elif language == "cpp":
        create_template_cpp(file_path)
    else:
        with open(file_path, "w") :
            pass

    os.system(f"code {file_path}")

    return


def create_template_py(output):
    try:
        copy_file(PYTHON_TEMPLATE_PATH, output)
    except Exception as e:
        print("Error occurred while copying : ", e)

    return


def create_template_cpp(output):
    try:
        copy_file(CPP_TEMPLATE_PATH, output)
    except Exception as e:
        print("Error occurred while copying : ", e)

    return


def is_valid_cstr(cstr):
    if len(cstr.split("/")) != 3:
        return False

    folder, _, language = cstr.split("/")

    if not any(x in folder for x in ALLOWED.keys()) or language not in ALLOWED_EXT:
        return False

    return True


def main():
    parser = argparse.ArgumentParser(description="A simple template generating tool")

    parser.add_argument("--cstr", type=str, help="Output file")

    args = parser.parse_args()

    if is_valid_cstr(args.cstr.strip()):
        create_template(args.cstr.strip())
    else:
        return


if __name__ == "__main__":
    main()
