import os
import argparse
from git import Repo


def extract_file_name(file):
    filename = file.split("/")[1]
    if (filename.startswith("_")):
        filename = filename[1:]
    return filename


def ignore_git_errors(func):

    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            pass
            # print(f'[WARNING] : {func.__name__}, {e}')

    return wrapper


class GitHelper:

    def __init__(self, repository_path):
        self.repository_path = repository_path
        self.repo = Repo(self.repository_path)
        self.commit_message = ""
        self.NOT_ALLOWED = [".git"]
        self.folders = []
        self.status = {}

        self.set_all_status()
        self.set_all_folders()

    def set_all_folders(self):
        for directory in os.listdir(os.path.abspath("../")):
            abs_path = os.path.realpath(os.path.join('..', directory))
            if (directory not in self.NOT_ALLOWED and os.path.isdir(abs_path)):
                if (directory not in self.folders):
                    self.folders.append(directory)
                    self.status["Untracked"][directory] = []
                    self.status["Modified"][directory] = []
                    self.status["Staged"][directory] = []

    def set_all_status(self):
        self.status["Untracked"] = {}
        self.status["Modified"] = {}
        self.status["Staged"] = {}

    @ignore_git_errors
    def set_untracked_files(self):
        temp = set()
        for file in self.repo.untracked_files:
            for folder_name in self.folders:
                if (folder_name in file):
                    filename = extract_file_name(file)
                    if (filename.split('.')[0] in temp):
                        continue
                    temp.add(filename.split('.')[0])
                    self.status["Untracked"][folder_name].append(filename)

    @ignore_git_errors
    def set_modified_files(self):
        temp = set()
        for item in self.repo.index.diff(None):
            file = item.a_path
            for folder_name in self.folders:
                if (folder_name in file):
                    filename = extract_file_name(file)
                    if (filename.split('.')[0] in temp):
                        continue
                    temp.add(filename.split('.')[0])
                    self.status["Modified"][folder_name].append(filename)

    @ignore_git_errors
    def set_staged_files(self):
        temp = set()
        for item in self.repo.index.diff("Head"):
            file = item.a_path
            for folder_name in self.folders:
                if (folder_name in file):
                    filename = extract_file_name(file)
                    if (filename.split('.')[0] in temp):
                        continue
                    temp.add(filename.split('.')[0])
                    self.status["Staged"][folder_name].append(filename)

    def set_commit_message(self, options):
        if (options.get("s")):
            self.set_staged_files()
        if (options.get("u")):
            self.set_untracked_files()
        if (options.get("m")):
            self.set_modified_files()

        self.untracked_message = "add: "
        self.staged_message = "stage: "
        self.modified_message = "update: "

        for k, v in self.status.items():
            for folder, files in v.items():
                if (len(files) > 0):
                    message = "(" + folder.lower() + ") " + ", ".join(files)
                    if (k == "Untracked"):
                        self.untracked_message += (message + " | ")
                    elif (k == "Staged"):
                        self.staged_message += (message + " | ")
                    elif (k == "Modified"):
                        self.modified_message += (message + " | ")

        if (self.untracked_message != "add: "):
            self.commit_message += self.untracked_message
        if (self.staged_message != "stage: "):
            self.commit_message += self.staged_message
        if (self.modified_message != "update: "):
            self.commit_message += self.modified_message

    def get_all_folders(self):
        return self.folders

    def get_status(self):
        return self.status

    def get_commit_message(self):
        self.commit_message = self.commit_message.strip().replace("  ", " ")
        if (self.commit_message.endswith("|")):
            self.commit_message = self.commit_message[:-1]
        return self.commit_message


class CLI:
    def __init__(self):
        self.parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                              description="Parameters for commit message", allow_abbrev=True, add_help=True)

        self.parser.add_argument(
            "-s", help="Include staged files", action="store_true")
        self.parser.add_argument(
            "-u", help="Include untracked files", action="store_false")
        self.parser.add_argument(
            "-m", help="Include modified files", action="store_true")

    def get_args(self):
        return self.parser.parse_args()


if __name__ == "__main__":

    repo_path = os.path.realpath(os.pardir)
    gh = GitHelper(repo_path)

    cli_args = CLI().get_args()
    options = {
        "s": cli_args.s,
        "u": cli_args.u,
        "m": cli_args.m,
    }
    gh.set_commit_message(options)
    print(gh.get_commit_message())
