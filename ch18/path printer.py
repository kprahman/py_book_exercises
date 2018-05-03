import os

def get_dirlist(path):
    dirlist = os.listdir(path)
    dirlist.sort()
    return dirlist

def path_printer(path):
    dirlist = get_dirlist(path)

    for f in dirlist:
        fullname = os.path.join(path,f)
        if os.path.isdir(fullname):
            path_printer(fullname)
        else:
            print(fullname)

def make_trash(path,trash):
    dirlist = get_dirlist(path)
    for f in dirlist:
        fn = os.path.join(path,f)
        if os.path.isdir(fn):
            trash_file = open(fn+"/"+trash+".txt","w")
            trash_file.close()
            make_trash(fn, trash) ## look for descendants

def take_out_the_trash(path,trash):
    dirlist = get_dirlist(path)
    for f in dirlist:
        fn = os.path.join(path, f)
        if os.path.isdir(fn):
            os.remove(fn+"/"+trash+".txt")


