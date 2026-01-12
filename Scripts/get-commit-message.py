import subprocess
from collections import defaultdict
import os

result = subprocess.run(
    ["git", "status", "--porcelain", "--untracked-files=all"],
    stdout=subprocess.PIPE,
    text=True,
)

adds = defaultdict(set)
mods = defaultdict(list)
dels = defaultdict(list)

for line in result.stdout.strip().splitlines():
    status_code = line[:2]
    path = line[3:].strip()
    parts = path.split(os.sep)

    if len(parts) > 2:
        top_folder = parts[0]
        sub_folder = parts[1]
    elif len(parts) > 1:
        top_folder = parts[0]
        sub_folder = parts[1]
    else:
        top_folder = "root"
        sub_folder = parts[0]

    if status_code in ("A ", "??"):
        adds[top_folder].add(sub_folder)
    elif status_code in (" M", "M "):
        mods[top_folder].append(sub_folder)
    elif status_code in (" D", "D "):
        dels[top_folder].append(sub_folder)


def print_section(label, section):
    for folder in sorted(section):
        entries = sorted(section[folder])
        if folder == ".":
            print(f"gcmsg '{label}: {', '.join(entries)}'")
        elif label == "add" and folder == "codeforces":
            print(f"gcmsg '{label}: ({folder}) {', '.join(entries)}'")
        else:
            print(f"gcmsg '{label}: ({folder}) {', '.join(entries)}'")


print_section("add", adds)
print_section("modify", mods)
print_section("delete", dels)
