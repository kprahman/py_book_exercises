def replace(old,new,s):
    w = s.split(old)

    list_of_words = []
    for (i,v) in enumerate(w):
        if i < (len(w)-1):
            split_word = list(v)
            split_word.append(new)
            complete_word = "".join(split_word)
            list_of_words.append(complete_word)
        else:
            list_of_words.append(v)
    final_string = "".join(list_of_words)
    return final_string







