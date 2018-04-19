def reverse_file(oldfile,newfile):

    myfile = open(oldfile, "r")
    xs = myfile.readlines()
    myfile.close()

    xs.reverse()

    writefile = open(newfile, "w")
    for v in xs:
        writefile.write(v)

    writefile.close()
