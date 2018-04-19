pre_num = open("text_of_snake.txt", "r")
xs = pre_num.readlines()
pre_num.close()

post_num = open("numbered_snake.txt", "w")
for (i,v) in enumerate(xs):
    i_string = "{:04d}".format(i)
    post_num.write("{0:<5}{1}".format(i_string + " ",v))
post_num.close()


