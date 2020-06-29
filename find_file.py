import sys
import os

def find_files(filename, search_path):
    result = []
    for root, dir, files in os.walk(search_path):
        if filename in files:
            result.append(filename)
    return result

print(find_files('notepad.exe', 'C:/Program Files'))