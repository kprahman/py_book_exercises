import string

def cleanword(s):
    new_word = []
    w = list(s)
    for (i,v) in enumerate(w):
        if v not in string.punctuation:
            new_word.append(v)
    last_word = "".join(new_word)
    return last_word

def has_dashdash(s):
    return "--" in s

def extract_words(phrase):
    x = phrase.split()
    final = []
    for (i,v) in enumerate(x):
        if has_dashdash(v):
            redo = v.split("--")
            for i in redo:
                x.append(i)
            continue
        cleaned = cleanword(v)
        cleaned = cleaned.lower()
        final.append(cleaned)
    return final

def wordcount(target, options):
    y = options.count(target)
    return y

def wordset(set):
    final = []
    for (i,v) in enumerate(set):
        if v not in final:
            final.append(v)
    final.sort()
    return final

def longestword(set):
    length = []
    for (i,v) in enumerate(set):
        x = len(v)
        length.append(x)
    if len(length) == 0:
        return 0
    y = max(length)
    return y

from unit_tester import test
test(longestword(["a", "apple", "pear", "grape"]) == 5)
test(longestword(["a", "am", "I", "be"]) == 2)
test(longestword(["this","supercalifragilisticexpialidocious"]) == 34)
test(longestword([ ]) == 0)