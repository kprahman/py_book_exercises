import string

letter = string.ascii_letters

file =open("numbered_snake.txt","r")
xs = file.readlines()
file.close()

outfile = open("joesagenius.txt", "w")
for l in xs:
    cutoff = l.index(" ") + 1
    outfile.write(l[cutoff:])
outfile.close()

