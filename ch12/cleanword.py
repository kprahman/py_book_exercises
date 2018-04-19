import string

set = ["a", "apple", "pear", "grape"]

def longestword(set):
    length = []
    for (i,v) in enumerate(set):
        x = len(v)
        length.append(x)
    return max(length)













