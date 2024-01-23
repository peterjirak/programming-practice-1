from list_merge_two_sorted_lists import list_merge_two_sorted_lists

def test_list_merge_two_sorted_lists_ascending():
    l1 = [ 5, 9, 13, 17, 23, 27, 33, 37, 43, 47 ]
    l2 = [ 3, 7, 15, 15, 15, 16, 17, 18, 19, 23, 27, 29, 31, 36, 39, 41, 45, 48 ]
    merged = list_merge_two_sorted_lists(l1, l2)
    assert merged == [3, 5, 7, 9, 13, 15, 15, 15, 16, 17, 17, 18, 19, 23, 23, 27, 27, 29, 31, 33, 36, 37, 39, 41, 43, 45, 47, 48], (
          "list_merge_two_sorted_lists correctly merged two lists")

def test_list_merge_two_sorted_lists_descending():
    l1 = [ 47, 43, 37, 33, 27, 23, 17, 13, 9, 5 ]
    l2 = [ 48, 45, 41, 39, 36, 31, 29, 27, 23, 19, 18, 17, 16, 15, 15, 15, 7, 3 ]
    merged = list_merge_two_sorted_lists(l1, l2)
    assert merged == [48, 47, 45, 43, 41, 39, 37, 36, 33, 31, 29, 27, 27, 23, 23, 19, 18, 17, 17, 16, 15, 15, 15, 13, 9, 7, 5, 3], (
          "list_merge_two_sorted_lists correctly merged two lists")