from list_merge_sorted_lists import merge_sorted_lists

def test_merge_sorted_lists_merge_two_ascending_sorted_lists():
    l1 = [ 5, 9, 13, 17, 23, 27, 33, 37, 43, 47 ]
    l2 = [ 3, 7, 15, 15, 15, 16, 17, 18, 19, 23, 27, 29, 31, 36, 39, 41, 45, 48 ]
    merged = merge_sorted_lists(l1, l2)
    assert merged == [3, 5, 7, 9, 13, 15, 15, 15, 16, 17, 17, 18, 19, 23, 23, 27, 27, 29, 31, 33, 36, 37, 39, 41, 43, 45, 47, 48], (
          "merge_sorted_lists correctly merged two sorted, ascending lists")

def test_merge_sorted_lists_merge_two_descending_sorted_lists():
    l1 = [47, 43, 37, 33, 27, 23, 17, 13, 9, 5]
    l2 = [48, 45, 41, 39, 36, 31, 29, 27, 23, 19, 18, 17, 16, 15, 15, 15, 7, 3]
    merged = merge_sorted_lists(l1, l2)
    assert merged == [48, 47, 45, 43, 41, 39, 37, 36, 33, 31, 29, 27, 27, 23, 23, 19, 18, 17, 17, 16, 15, 15, 15, 13, 9, 7, 5, 3], (
           "merge_sorted_lists correctly merged two sorted, descending lists"
    )

# if __name__ == '__main__':
#     test_merge_sorted_lists_merge_two_descending_sorted_lists()
