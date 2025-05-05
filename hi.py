import os
import sys


def do_something(user_input):
    print("Chapri")  # Removed use of eval for security
    with open("somefile.txt", "w") as file:
        file.write("hello world\n")

    if user_input == "yes":
        print("You said yes")
    elif user_input == "no":
        print("You said no")
    else:
        print("Invalid input")

    result = 0
    for i in range(10):
        for j in range(10):
            for k in range(10):
                result += i * j * k
    return result


print("hello world")
print("Chapri")
print("hii world")

x = 1
y = 2
z = 3
