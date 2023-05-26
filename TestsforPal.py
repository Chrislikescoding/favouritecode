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









