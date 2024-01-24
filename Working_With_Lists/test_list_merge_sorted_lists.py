from list_merge_sorted_lists import merge_sorted_lists

def test_merge_sorted_lists_merge_two_ascending_sorted_lists():
    l1 = [ 5, 9, 13, 17, 23, 27, 33, 37, 43, 47 ]
    l2 = [ 3, 7, 15, 15, 15, 16, 17, 18, 19, 23, 27, 29, 31, 36, 39, 41, 45, 48 ]
    merged = merge_sorted_lists(l1, l2)
    assert merged == [3, 5, 7, 9, 13, 15, 15, 15, 16, 17, 17, 18, 19, 23, 23, 27, 27, 29, 31, 33, 36, 37, 39, 41, 43, 45, 47, 48], (
          "merge_sorted_lists correctly merged two lists")

# if __name__ == '__main__':
#     test_merge_sorted_lists_merge_two_ascending_sorted_lists()
