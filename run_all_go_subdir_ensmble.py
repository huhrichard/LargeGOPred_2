import os, fnmatch
import sys
from os import remove, system
from os.path import abspath

import glob

def find_dir(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if fnmatch.fnmatch(dir, pattern):
                result.append(abspath(os.path.join(path, dir)))

    return result

if __name__ == "__main__":
    file_list = find_dir('GO*',sys.argv[-1])
    for go_file in file_list:
        python_cmd = 'python ensemble.py --path {}'.format(go_file)
        print(python_cmd)
        system(python_cmd)
