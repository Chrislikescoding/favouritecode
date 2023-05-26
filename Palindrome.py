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

# TypeError print(is_palindrome(12321))
# I am including a palindromic number
print(is_palindrome("malayalam"))
print(is_palindrome("Eva, can I see bees in a cave?"))

print(is_palindrome("?><{}!?"))

print(is_palindrome("was it a car or a cat I saw?") )


print(is_palindrome('12321'))
# I am including a palindromic number but in the form of a string
# a quick palindrome solution bbut does not work for whitepace or punctuation
word1 = "malayalam"
#print(word1 == word1[::-1])

pal= "Eva, can I see bees in a cave?"
#print(pal.lower() == pal.lower()[::-1])