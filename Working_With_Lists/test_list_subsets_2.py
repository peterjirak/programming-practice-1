
from list_subsets_2 import subset_sums_to_zero

def test_subset_sums_to_zero():
    integer_list = [ -48, 9, 11, 23, 27, -15, 43, 58, -17, 78, -24 ]
    result = subset_sums_to_zero(integer_list)
    assert len(result) > 0, "A subset with more than zero integers was returned"
    total = sum(result)
    assert total == 0, "The sum of the subset of integers is zero"
    not_found_count = 0
    for num in result:
        if num not in integer_list:
            not_found_count += 1
    assert not_found_count == 0, "All of the integers in the subset were in the argument integer list"
