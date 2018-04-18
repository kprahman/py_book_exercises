import module1
import module2

birthday_yet = (module2.myage - module1.myage) ==\
               (module2.year - module1.year)

print("My name is", __name__)


if birthday_yet:
    print("you've already had your birthday!")
else:
    print("get ready for ur big day")


