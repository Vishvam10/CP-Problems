import os

NOT_ALLOWED = [".git", "README.md", "Scripts"] 

for directory in os.listdir(os.path.abspath("../")) :
    if(directory not in NOT_ALLOWED) :
        abs_path = "../{}".format(directory)
        for file in os.listdir(abs_path):
            new_name = "{}.py".format(file.replace(
                " ", "_").replace("-", "_").replace(",", "").lower().split(".")[0])

            os.rename(os.path.join(abs_path, file), os.path.join(abs_path, new_name))
