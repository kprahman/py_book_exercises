import string

letters = string.ascii_letters

infile = open("numbered_snake.txt", "r")
xs = infile.readlines()
infile.close()

outfile = open("numberless_snake.txt", "w")
for v in xs:
    split_original = list(v)
    for (i,v) in enumerate(split_original):
        while v not in letters:
            split_original.remove(v)
            continue
        raw_final="".join(split_original)
        outfile.write(raw_final)
outfile.close()






