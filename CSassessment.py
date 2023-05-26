# Task 3 Write a function called is_palindrome
# palindrome is a word that can be written backwards or forwards and is the same
# it is possible to test for palindrome just by reversing a string, but this does
# a quick palindrome solution but does not work for whitepace or punctuation marks
# so the second string below does not work

word1 = "malayalam"
print(word1 == word1[::-1])

pal= "Eva, can I see bees in a cave?"
print(pal.lower() == pal.lower()[::-1])

def is_palindrome(word):
    letters = [char.lower() for char in word if char != ' ' and char.isalnum()]
    is_palindrome  = len(letters) != 0
    i = 0
    while len(letters) > 0 and is_palindrome:
        if letters[0] != letters[(len(letters) - 1)]:
            is_palindrome = False
        else:
            letters.pop(0)
            if len(letters) > 0:
                letters.pop((len(letters) - 1))

    return is_palindrome

# I dont know if a number should be included but I am included a palindromic number
print(is_palindrome('12321'))
print(is_palindrome("?><{}!?"))
print(is_palindrome("malayalam"))
print(is_palindrome("was it a car or a cat I saw?") )
print(is_palindrome("Eva, can I see bees in a cave?"))

#Task 4

from unittest import TestCase, main # for all examples
from CSassessment import is_palindrome

class test_valid_(TestCase):
# this is a valid
# a valid palindrome - the "happy path" - I want to first see that it does actually work for a palindrome
    def test_happy_valid(self):
        expected = True
        result = is_palindrome("malayalam")
        self.assertEqual(expected, result)

class test_not_valid_(TestCase):
#not a valid palindrome so for this test I want to see that my code will detect a non palindrome
    def test_happy_valid(self):
        expected = False
        result = is_palindrome("I am not a palindrome")
        self.assertEqual(expected, result)

#this test is to show that my code will work with punctuation marks in the sentence, or special characters
class test_valid_withspc(TestCase):
# a valid palindrome with special characters
    def test_valid_withspc(self):
        expected = True
        result = is_palindrome("Eva, can I see bees in a cave?")
        self.assertEqual(expected, result)

# a white spaces entry - I want to test what happens with white spaces
    class test_pal_withwpc(TestCase):

        def test_happy_valid(self):
            expected = False
            result = is_palindrome("     ")
            self.assertEqual(expected, result)

# a number as a string, to check that I can process numeric strings
    class test_pal_withalnum(TestCase):

        def test_happy_valid(self):
            expected = True
            result = is_palindrome("12321")
            self.assertEqual(expected, result)

# Task 9

def two_number_sum(numbers,target):
    used_numbers=[]
    for number in numbers:
        search_number = target - number
        if search_number in used_numbers:
            return[number,search_number]
        used_numbers.append(number)
    return []

#possible
numbers = [3, 5, -4, 8, 11, 1, -1]
target = 10
result = two_number_sum(numbers, target)
#possible
numbers = [1, 2, 4, 2, 1, 45, 51, 24]
target = 3
result = set(two_number_sum(numbers, target))
print(result)

#not possible
numbers = [1, 2, 4, 2, 1, 45, 51, 24]
target = 27
result = two_number_sum(numbers, target)
print(result)