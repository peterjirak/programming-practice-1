import re

"""
there_is_a_permutation_that_is_a_palindrome(argument)

ARGUMENTS
1. argument - a string

RETURNS
True if there is a permutation of the string that is a palindrome
False if there are no permutations of the string that are a palindrome

DESCRIPTION
It takes in a string and returns True if there is a permutation of the string
that is a palindrome and false otherwise
"""
def there_is_a_permutation_that_is_a_palindrome(argument):
    argument = str(argument)
    argument = re.sub(r'[^A-Za-z0-9]', '', argument)
    argument = argument.lower()
    char_counts = {}
    for char in argument:
        if not char_counts.get(char):
            char_counts[char] = 1
        else:
            char_counts[char] += 1

    chars = char_counts.keys()
    if len(chars) == 1:
        return True
    even_count = 0
    odd_count = 0
    for char in chars:
        if char_counts[char] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    if odd_count == 0:
        return True
    elif odd_count > 1:
        return False
    else:
        if len(argument) % 2 == 0:
            return False
        else:
            return True