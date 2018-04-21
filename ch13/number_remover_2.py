import string

letters = string.ascii_letters

infile = open("numbered_snake.txt", "r")
xs = infile.readlines()
infile.close()
print(type(xs))

outfile = open("numberless_snake2.txt", "w")
for v in xs:
    counter = 0
    if
    while v[counter] not in letters:
        if counter == len(v)-1:
            break
        counter += 1
        continue
    if v[counter - 2] == " ":
        slicey = ("0:first_space + 1")
        outfile.write(v[int(slicey):])
    else:
        outfile.write(v[counter:])

outfile.close()

