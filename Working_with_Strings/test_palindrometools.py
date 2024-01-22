from palindrometools import there_is_a_permutation_that_is_a_palindrome

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
