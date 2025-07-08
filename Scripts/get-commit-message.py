import subprocess
from collections import defaultdict
import os

result = subprocess.run(
    ["git", "status", "--porcelain"],
    stdout=subprocess.PIPE,
    text=True
)

adds = defaultdict(set)
mods = defaultdict(list)
dels = defaultdict(list)

for line in result.stdout.strip().splitlines():
    status_code = line[:2]
    path = line[3:].strip()
    parts = path.split(os.sep)

    filename = parts[-1]
    if len(parts) > 2:
        top_folder = parts[0].lower()
        subfolder = parts[1]
    elif len(parts) > 1:
        top_folder = parts[0].lower()
        subfolder = "."
    else:
        top_folder = "."
        subfolder = "."

    if status_code in ("A ", "??"):
        if top_folder == "codeforces":
            adds[top_folder].add(subfolder)
        else:
            adds[top_folder].add(filename)
    elif status_code in (" M", "M "):
        mods[top_folder].append(filename)
    elif status_code in (" D", "D "):
        dels[top_folder].append(filename)

def print_section(label, section, show_files=True):
    for folder in sorted(section):
        entries = sorted(section[folder])
        if folder == ".":
            print(f"{label}: {', '.join(entries)}")
        elif label == "add" and folder == "codeforces":
            print(f"{label}: ({folder}) {', '.join(entries)}")
        else:
            print(f"{label}: ({folder}) {', '.join(entries)}")

print_section("add", adds)
print_section("modify", mods)
print_section("delete", dels)
