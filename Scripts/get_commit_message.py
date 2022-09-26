import os
import argparse
from git import Repo


# for x in repo.git.status().split("Untracked files")[1].split("\n") :
#     print(x)

class GitHelper :
    def __init__(self, repository_path):
        self.repository_path = repository_path
        self.repo = Repo(self.repository_path)

    def get_untracked_files(self) :
        return self.repo.untracked_files

    def get_modified_files(self) :
        f = []
        for item in self.repo.index.diff(None):
            f.append(item.a_path)
        return f

    def get_staged_files(self) :
        f = []
        for item in self.repo.index.diff("Head"):
            f.append(item.a_path)
        return f

    def get_commit_message(self, options) :
        files = []
        if(options.get("s")) :
            files.append(self.get_staged_files())
        if(options.get("u")) :
            files.append(self.get_untracked_files())
        if(options.get("m")) :
            files.append(self.get_modified_files())

        print("FILES AFFECTED : ", files)

class CLI :
    def __init__(self) :
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter, description="Parameters for commit message", allow_abbrev=True, add_help=True)
        
        self.parser.add_argument("-s", help="Include staged files", action="store_true")
        self.parser.add_argument("-u", help="Include untracked files",action="store_false")
        self.parser.add_argument("-m", help="Include modified files", action="store_true")
    
    def get_args(self) :
        return self.parser.parse_args()
    
    

if __name__ == "__main__" :

    repo_path = os.pardir
    gh = GitHelper(repo_path)

    cli_args = CLI().get_args()
    options = {
        "s": cli_args.s,
        "u": cli_args.u,
        "m": cli_args.m,
    }
    gh.get_commit_message(options)


