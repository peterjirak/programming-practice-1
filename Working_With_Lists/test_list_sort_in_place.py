from list_sort_in_place import sort_in_place

def test_sort_in_place_ten_integers_ascending():
    items = [ 31, 5, 75, 3, 25, 45, 80, 4, 93, 7 ]
    sort_in_place(items, ascending=True)
    assert items == [3, 4, 5, 7, 25, 31, 45, 75, 80, 93], "Successfully sorted in ascending order a list of ten integers"

def test_sort_in_place_ten_integers_descending():
    items = [ 31, 5, 75, 3, 25, 45, 80, 4, 93, 7 ]
    sort_in_place(items, ascending=False)
    assert items == [93, 80, 75, 45, 31, 25, 7, 5, 4, 3], "Successfully sorted in descending order a list of ten integers"

# if __name__ == '__main__':
#     test_sort_in_place_ten_integers_descending()
