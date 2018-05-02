import os

def get_dirlist(path):
    """Return a sorted list of all entires in a path.
    Return just the names, not the full path to names"""
    dirlist =  os.listdir(path)
    dirlist.sort()
    return dirlist

def print_files(path, prefix = ""):
    """Print recursive listing of path contents"""
    if prefix == "":
        print("Folder listing for", path) ## the name of argument path
        prefix = "| "

    dirlist = get_dirlist(path)
    for f in dirlist:
        print(prefix+f)
        fullname = os.path.join(path,f)
        if os.path.isdir(fullname):  ## tests to see whether the path is a directory.
            print_files(fullname, prefix + "| ") ## if path is a directory, print child files with an extra indent.

print_files("/home/kprahman/PycharmProjects/py_book_exercises/ch18")