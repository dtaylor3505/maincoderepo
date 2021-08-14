name = "Kay"
number = len(name) * 9
print("Hello " + name + " .Your lucky number is " + str(number))

name = "DeShaon"
number = len(name) * 9
print("Hello " + name + " .Your lucky number is " + str(number))

#This is the same script as above but with a function


def luckynumber(name):
    number = len(name) * 9
    print("Hello " + name + " .Your lucky number is " + str(number))

luckynumber("Kay")
luckynumber("DeShaon")
