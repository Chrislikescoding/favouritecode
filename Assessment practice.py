#SQL

# ALTER table Student
# ADD PRIMARY KEY (s_id);
# https://www.studytonight.com/dbms/sql-constraints.php

# CREATE table Order_Detail(
#     order_id int PRIMARY KEY,
#     order_name varchar(60) NOT NULL,
#     c_id int FOREIGN KEY REFERENCES Customer_Detail(c_id)
# );

# ALTER table Order_Detail
# ADD FOREIGN KEY (c_id) REFERENCES Customer_Detail(c_id);

# Constraints are used to make sure that the integrity of data is maintained in the database. Following are the most used constraints that can be applied to a table.
#
# NOT NULL
# UNIQUE
# PRIMARY KEY
# FOREIGN KEY
# CHECK
# DEFAULT

# ALTER TABLE Student
# MODIFY s_id int NOT NULL;

# CREATE table Student
# (	s_id int PRIMARY KEY,
# 	Name varchar(60) NOT NULL,
# 	Age int);

# ALTER table Order_Detail
# ADD FOREIGN KEY (c_id) REFERENCES Customer_Detail(c_id);

# Python

# - Write a function that accepts an array of number and an integer representing a target sum.
# - If any two numbers from the accepted numbers sum up to the target sum then the function should return them in array,
# in any order.
# - If no numbers sum to the target sum, the function should return an empty array.
# - The target has to be achieved using different numbers from the array.


def find_target_sum(numbers,target):
    used_numbers=[]
    for number in numbers:
        search_number = target - number

        if search_number in used_numbers:
            return[number,search_number]
        used_numbers.append(number)
    return []

numbers = [3, 5, -4, 8, 11, 1, -1]
target = 10

result = find_target_sum(numbers, target)
print(result)

# # # Question 3. Write a function that can define whether a word is a Palindrome or not  (a word, phrase, or sequence
# # # that reads the same backwards as forwards, e.g. madam)

# def define_palindrome():
#     reversed_palindrome = palindrome[::-1]
#     is_palindrome = False
#     if (palindrome == reversed_palindrome):
#         is_palindrome = True
#     return is_palindrome


# palindrome = input("Enter the word to test for a palindrome: ")
# is_palindrome = define_palindrome()
# if is_palindrome:
#     print("It is a palindrome!")
# else:
#     print("Sorry! That is not a palindrome!")


# s = '2020-11-10_sales.csv'
# sliced = s[0:16]
# print(sliced)

#
# with open ('clients.txt','r') as f:
#     x = 0
#     content = f.read()
#     for char in content:
#         if char.isupper():
#             x+=1
#
#
# print ("x " + str(x))

# today = input('What day is it? ')
# is_monday = today == 'Monday'
# print('Today is Monday: {}'.format(is_monday))

# from operator import *
# calc = {
#     "+": add,
#     "-": sub,
#     "*": mul,
#     "**": pow,
#     "/": truediv,
#     "//": floordiv,
#     "%": mod
# }


#print(calc[op](first_num, second_num))
calc = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "**": lambda a, b: a ** b,
    "/": lambda a, b: a / b,
    "//": lambda a, b: a // b,
    "%": lambda a, b: a % b
}

first_num = int(input("Please enter your first number?: "))
second_num = int(input("Please enter your second number?: "))
op = input("Select an operation add,subtract,multiply,exponent,divide,floor,modulus \n "
           "                     (+     -      *        **       /     //     %): ")
print(calc[op](first_num, second_num))
# def say():
#     greeting = 'Hello'
#
#     def display():
#         print(greeting)

#    display()
# embedded functions in python are an example of closures
# in Go, I do var myFunc := func() { /* lines */ }()
