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

"""
palindrome_checker(input_string)
ARGUMENTS
1. input_string - String to test

RETURNS
 * The string if it is a palindrome or the palindrome created by deleting one
   character from the string.
 * None if the string is not a palindrome and deleting one character from the
   string would not make it a palindrome.

DESCRIPTION
Check to see if the string is a palindrome. If the string is not a palindrome,
check to see if deleting one character from the string would make it a palindrome.

If thew string is a palindrome or if deleting one character from the string would
make  it a palindrome, return the palindrome. If it is not a palindrome and
deleting one character would not make it a palindrome, then return None

NOTES
 * When checking for a palindrome we ignore all characters that are not letters
   and not numbers - like spaces and punctuation.
"""
def palindrome_checker(input_string):
    left = 0
    right = len(input_string) - 1
    skipped = None
    while left < right:
        if not input_string[left].isalnum():
           left += 1
        elif not input_string[right].isalnum():
           right -= 1
        elif input_string[left].lower() != input_string[right].lower():
            if skipped is not None:
                return None
            else:
                check_right = right - 1
                while left < check_right and not input_string[check_right].isalnum():
                    check_right -= 1
                if input_string[left].lower() == input_string[check_right].lower():
                    skipped = right
                    right = check_right
                    continue
                check_left = left + 1
                while check_left < right and not input_string[check_left].isalnum():
                    check_left += 1
                if input_string[check_left].lower() == input_string[right].lower():
                    skipped = left
                    left = check_left
                    continue
                return None
        else:
            left += 1
            right -= 1
    if skipped is None:
        return input_string
    else:
        return input_string[:skipped] + input_string[skipped + 1:]
