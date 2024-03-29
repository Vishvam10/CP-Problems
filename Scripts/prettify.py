import hashlib
import os
import subprocess
import sys
from pathlib import Path

import autopep8

current_dir = os.getcwd()
root_dir = os.path.dirname(current_dir)
templates_dir = os.path.join(root_dir, 'Templates')

ALLOWED_DIRS = ['CodeForces', 'CodeStudio', 'LeetCode',
                'GeeksForGeeks', 'Scripts', 'Templates']


def hash_file(file_path):
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(4096):
            hasher.update(chunk)
    return hasher.hexdigest()


def prettify_cpp_files(directory, processed_files):

    cpp_files = [os.path.join(root, file) for root, _, files in os.walk(directory) for file in files if file.endswith(
        '.cpp') and any(allowed_dir in root for allowed_dir in ALLOWED_DIRS)]

    # Filter out files that have already been processed
    cpp_files_to_process = [
        file for file in cpp_files if hash_file(file) not in processed_files]

    for cpp_file in cpp_files_to_process:
        try:
            subprocess.run(['clang-format', '-i', cpp_file], check=True)
            print(f'Prettified: {cpp_file}')
            processed_files.add(hash_file(cpp_file))
        except Exception as e:

            print(f'Error prettifying {cpp_file}: {e}')


def prettify_python_files(directory, processed_files):

    python_files = [os.path.join(root, file) for root, _, files in os.walk(
        directory) for file in files if file.endswith('.py') and any(allowed_dir in root for allowed_dir in ALLOWED_DIRS)]

    # Filter out files that have already been processed
    python_files_to_process = [
        file for file in python_files if hash_file(file) not in processed_files]

    for python_file in python_files_to_process:
        try:
            # Read the content of the file
            with open(python_file, 'r') as f:
                content = f.read()

            # Auto-format the content
            formatted_content = autopep8.fix_code(content)

            # Write the formatted content back to the file
            with open(python_file, 'w') as f:
                f.write(formatted_content)

            print(f'Prettified: {python_file}')
            # Add the file's hash to the processed files record
            processed_files.add(hash_file(python_file))
        except Exception as e:
            print(f'Error prettifying {python_file}: {e}')


def read_processed_files_record(record_file):
    processed_files = set()
    if os.path.isfile(record_file):
        with open(record_file, 'r') as f:
            for line in f:
                processed_files.add(line.strip())
    return processed_files


def write_processed_files_record(record_file, processed_files):
    with open(record_file, 'w') as f:
        for file_hash in processed_files:
            f.write(file_hash + '\n')


if __name__ == '__main__':
    codebase_directory = root_dir

    processed_files_record_file = './Scripts/prettify-cache.txt'
    processed_files = read_processed_files_record(processed_files_record_file)

    prettify_cpp_files(codebase_directory, processed_files)
    prettify_python_files(codebase_directory, processed_files)

    write_processed_files_record(processed_files_record_file, processed_files)
