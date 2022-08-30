import os

gfg = os.path.abspath('../GeeksForGeeks')

for file in os.listdir(gfg):
    new_name = "{}.py".format(file.replace(
        " ", "_").replace("-", "_").replace(",", "").lower().split(".")[0])

    os.rename(os.path.join(gfg, file), os.path.join(gfg, new_name))
