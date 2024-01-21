from listtools import insert_into

def test_insert_into_starting_with_an_empty_list_ten_items_ascending():
    items_to_insert = [ 31, 5, 75, 3, 25, 45, 80, 4, 93, 7 ]
    item_list = []
    for item in items_to_insert:
        insert_into(item_list, item)
    assert item_list == [3, 4, 5, 7, 25, 31, 45, 75, 80, 93], "Successfully inserted in ascending order ten items into a list"

# if __name__ == '__main__':
#    test_insert_into_starting_with_an_empty_list_ten_items_ascending()
