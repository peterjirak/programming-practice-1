from palindrometools import there_is_a_permutation_that_is_a_palindrome, palindrome_checker

def test_have_palindromes():
    has_palindromes = there_is_a_permutation_that_is_a_palindrome('Panama: a man, a plan, a canal')
    assert has_palindromes, "A permutation is a palindrome - 'Panama: a man, a plan, a canal'"
    has_palindromes = there_is_a_permutation_that_is_a_palindrome('eellv')
    assert has_palindromes, "A permutation is a palindrome - 'eekkv'"
    has_palindromes = there_is_a_permutation_that_is_a_palindrome('aradr')
    assert has_palindromes, "A permutation is a palindrome - 'aradr'"
    has_palindromes = there_is_a_permutation_that_is_a_palindrome('opp')
    assert has_palindromes, "A permutation is a palindrome - 'opp'"
    has_palindromes = there_is_a_permutation_that_is_a_palindrome('oopp')
    assert has_palindromes, "A permutation is a palindrome - 'oopp'"
    has_palindromes = there_is_a_permutation_that_is_a_palindrome('NASA - ata Santa')
    assert has_palindromes, "A permutation is a palindrome - 'NASA - ata Santa'"

def test_does_not_have_palindromes():
    has_palindromes = there_is_a_permutation_that_is_a_palindrome('Panda')
    assert not has_palindromes, "There are no permutations that are palindromes - 'Panda'"
    has_palindromes = there_is_a_permutation_that_is_a_palindrome('Lucy')
    assert not has_palindromes, "There are no permutations that are palindromes - 'Lucy'"
    has_palindromes = there_is_a_permutation_that_is_a_palindrome('New Orleans')
    assert not has_palindromes, "There are no permutations that are palindromes - 'New Orleans'"
    has_palindromes = there_is_a_permutation_that_is_a_palindrome('Minneapolis')
    assert not has_palindromes, "There are no permutations that are palindromes - 'Minneapolis'"

def test_palindrome_checker():
    assert palindrome_checker('A Man, a Plan, a Canal, Panama!') == 'A Man, a Plan, a Canal, Panama!', (
           "'A Man, a Plan, a Canal, Panama!' is a palindrome")

    assert palindrome_checker('racecar') == 'racecar', (
           "'racecar' is a palindrome")

    assert palindrome_checker('level') == 'level', (
           "'level' is a palindrome")

    assert palindrome_checker('levels') == 'level', (
           "'levels' is a palindrome after deleting the s")

    assert palindrome_checker('bracecar') == 'racecar', (
           "'bracecar' is a palindrome after deleting the b")

    assert palindrome_checker('Madfam') == 'Madam', (
           "'Madfam' is a palindrome after deleting the f")

    assert palindrome_checker('Madam, in Eden, I’m SAdam.') == 'Madam, in Eden, I’m Adam.', (
           "'Madam, in Eden, I’m Adam.' is a palindrome after deleting the S")



if __name__ == '__main__':
    test_palindrome_checker()