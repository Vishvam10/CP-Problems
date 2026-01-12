import os
import subprocess
import hashlib

# We go the abs way because this script can also be run as git-hook
# so the current for that changes and we don't want that
current_dir = os.path.abspath(".")
root_dir = os.path.abspath(os.path.join(current_dir, ".."))

ALLOWED_DIRS = [
    "CodeForces",
    "CodeStudio",
    "LeetCode",
    "GeeksForGeeks",
    "Scripts",
    "Templates",
]


def is_allowed_path(path: str) -> bool:
    return any(d in path for d in ALLOWED_DIRS)


def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


def has_cmd(cmd):
    return (
        subprocess.run(
            ["which", cmd],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        ).returncode
        == 0
    )


def prettify_cpp_files(directory, processed_files):
    if not has_cmd("clang-format"):
        print("clang-format not found, skipping C++ formatting")
        return

    for root, _, files in os.walk(directory):
        if not is_allowed_path(root):
            continue

        for file in files:
            if not file.endswith(".cpp"):
                continue

            cpp_file = os.path.join(root, file)
            file_hash = hash_file(cpp_file)

            if file_hash in processed_files:
                continue

            try:
                subprocess.run(["clang-format", "-i", cpp_file], check=True)
                print(f"Prettified C++: {cpp_file}")
                processed_files.add(hash_file(cpp_file))
            except Exception as e:
                print(f"Error prettifying {cpp_file}: {e}")


def prettify_python_files(directory):
    if not has_cmd("ruff"):
        print("ruff not found, skipping Python formatting")
        return

    try:
        subprocess.run(
            ["ruff", "format", directory, "--quiet"],
            check=False,  # Important: don't fail on parse errors
        )
        print(f"Prettified Python under: {directory}")
    except Exception as e:
        print(f"Error prettifying Python files: {e}")


def ensure_package_main(go_file_path):
    try:
        with open(go_file_path, "r") as f:
            lines = f.readlines()

        for line in lines:
            stripped = line.strip()
            if stripped == "" or stripped.startswith("//"):
                continue
            if stripped.startswith("package"):
                return
            break

        lines.insert(0, "package main\n")
        with open(go_file_path, "w") as f:
            f.writelines(lines)
        print(f"Inserted 'package main' in: {go_file_path}")

    except Exception as e:
        print(f"Error inserting package in {go_file_path}: {e}")


def prettify_go_files(directory):
    if not has_cmd("gofmt"):
        print("gofmt not found, skipping Go formatting")
        return

    for root, _, files in os.walk(directory):
        if not is_allowed_path(root):
            continue

        for file in files:
            if not file.endswith(".go"):
                continue

            go_file = os.path.join(root, file)

            # Auto-insert package main if missing
            ensure_package_main(go_file)

            try:
                subprocess.run(["gofmt", "-w", go_file], check=True)
                print(f"Prettified Go: {go_file}")
            except Exception as e:
                print(f"Error prettifying {go_file}: {e}")


def read_processed_files_record(record_file):
    processed_files = set()
    if os.path.isfile(record_file):
        with open(record_file, "r") as f:
            processed_files = {line.strip() for line in f}
    return processed_files


def write_processed_files_record(record_file, processed_files):
    with open(record_file, "w") as f:
        for file_hash in processed_files:
            f.write(file_hash + "\n")


if __name__ == "__main__":
    print("current dir :", current_dir)
    print("root dir :", root_dir)

    processed_files_record_file = "./prettify-cache.txt"
    processed_files = read_processed_files_record(processed_files_record_file)

    prettify_cpp_files(root_dir, processed_files)
    prettify_python_files(root_dir)
    prettify_go_files(root_dir)

    write_processed_files_record(processed_files_record_file, processed_files)
