string_mine = "ThiS is String with Upper and lower case Letters"

letter_count = {}

for letter in string_mine.lower():
    if letter is not " ":
        letter_count[letter] = letter_count.get(letter,0) + 1

letter_table = list(letter_count.items())
letter_table.sort() ##if list did not need to be alphabetized, could just use a for loop on letter_count.items

for i in letter_table:
    print("{0} | {1}".format(i[0],i[1]), end = "\n")



