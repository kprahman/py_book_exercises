import string

letters = string.ascii_letters

infile = open("numbered_snake.txt", "r")
xs = infile.readlines()
infile.close()
print(type(xs))

outfile = open("numberless_snake2.txt", "w")
for v in xs:
    counter = 0
    while v[counter] not in letters:
        if counter == len(v)-1:
            break
        counter += 1
        continue
    outfile.write(v[counter:])
outfile.close()

