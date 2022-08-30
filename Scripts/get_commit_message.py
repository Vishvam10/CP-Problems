import os
from git import Repo

repo_path = os.pardir
repo = Repo(repo_path)

commit_message = "Added {}".format(", ".join([x.replace("\n", "").replace("\t", "").split(".")[0].split("/")[1].lower() for x in repo.git.status().split("Untracked files")[1].split("\n")[2:-2]]))

print(commit_message)