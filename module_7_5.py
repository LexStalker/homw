import os
import time
directory = "."
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        last_modified_time = os.path.getmtime(file_path)
        file_size = os.path.getsize(file_path)
        parent_directory = os.path.dirname(file_path)
print(f"File: {file}")
print(f"Full path: {file_path}")
print(f"Last modified: {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(last_modified_time))}")
print(f"File size: {file_size} bytes")
print(f"Parent directory: {parent_directory}")
print()