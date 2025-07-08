import subprocess
from collections import defaultdict
import os

result = subprocess.run(
    ["git", "status", "--porcelain"],
    stdout=subprocess.PIPE,
    text=True
)

adds = defaultdict(list)
mods = defaultdict(list)
dels = defaultdict(list)

for line in result.stdout.strip().splitlines():
    status_code = line[:2]
    path = line[3:].strip()
    filename = os.path.basename(path)
    folder = os.path.basename(os.path.dirname(path)) or "."

    if status_code in ("A ", "??"):
        adds[folder].append(filename)
    elif status_code in (" M", "M "):
        mods[folder].append(filename)
    elif status_code in (" D", "D "):
        dels[folder].append(filename)

def print_section(label, section):
    for folder, files in section.items():
        file_list = ", ".join(files)
        if folder == ".":
            print(f"{label}: {file_list}")
        else:
            print(f"{label}: ({folder}) {file_list}")

print_section("add", adds)
print_section("modify", mods)
print_section("delete", dels)
