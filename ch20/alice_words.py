import time
def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.
    """

    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)
    wds = cleaned_text.split()
    return wds

##open alice, make a list out of all the words minus punctuation and capitals.
##PROBLEM: this splits up words like wouldn't into wouldn and t
t0 = time.clock()
f = open("alice.txt")
content = f.read()
f.close()
the_words = text_to_words(content)

##add dictionary keys
dictionary = {}
for i in the_words:
    if i not in dictionary: ##no repeat counting!
        dictionary[i] = the_words.count(i) ##find frequency

#got to turn this back into a list to alphabetize.
alpha_words = list(dictionary.items())
alpha_words.sort()

#write to a new file
g = open("alice_words.txt", "w")
dash = '-' * 31 + "\n"
for i in range(len(alpha_words)):
    if i == 0:
        g.write("{0:<30s}{1:s} \n".format("WORD", "COUNT"))
        g.write(dash)
    g.write("{0:<30s} {1:d} \n".format(alpha_words[i][0],alpha_words[i][1]))

g.close()
t1 = time.clock()
print("That took {} seconds to complete!".format(t1-t0))





