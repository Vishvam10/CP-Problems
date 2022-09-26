import os

NOT_ALLOWED = [".git", "README.md", "Scripts", "Topics"] 

def rename_files(folder, extension) :
    for directory in os.listdir(os.path.abspath("../")) :
        if(directory not in NOT_ALLOWED and directory == folder) :
            abs_path = "../{}".format(directory)
            for file in os.listdir(abs_path):
                formatted_name = standard_format(file).split(".")[0]
                new_name = "{}_{}.{}".format(folder, formatted_name, extension)

                os.rename(os.path.join(abs_path, file), os.path.join(abs_path, new_name))

def standard_format(s) :
    return s.replace(" ", "_")\
            .replace("-", "_")\
            .replace(",", "")\
            .lower()


def RenameLeetCodeDirectory() :
    folder = "LeetCode"
    extension = "py"
    rename_files(folder, extension)

if __name__ == "__main__" :
    RenameLeetCodeDirectory()