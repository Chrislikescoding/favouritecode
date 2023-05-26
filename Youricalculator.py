from operator import *
calc = {
    "+": add,
    "-": sub,
    "*": mul,
    "**": pow,
    "/": truediv,
    "//": floordiv,
    "%": mod
}

# calc = {
#     "+": lambda a, b: a + b,
#     "-": lambda a, b: a - b,
#     "*": lambda a, b: a * b,
#     "**": lambda a, b: a ** b,
#     "/": lambda a, b: a / b,
#     "//": lambda a, b: a // b,
#     "%": lambda a, b: a % b
# }
first_num = int(input("First number?: "))
second_num = int(input("Second number?: "))
op = input("Operation ? (+,-,*,**,/,//,%): ")

print(calc[op](first_num, second_num))

def say():
    greeting = 'Hello'

    def display():
        print(greeting)

    display()
# embedded functions in python are an example of closures
# in Go, I do var myFunc := func() { /* lines */ }()


