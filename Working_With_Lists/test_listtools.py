from listtools import insert_into

def test_insert_into_starting_with_an_empty_list_ten_integers_ascending():
    items_to_insert = [ 31, 5, 75, 3, 25, 45, 80, 4, 93, 7 ]
    item_list = []
    for item in items_to_insert:
        insert_into(item_list, item)
    assert item_list == [3, 4, 5, 7, 25, 31, 45, 75, 80, 93], "Successfully inserted in ascending order ten integers into a list"

def test_insert_into_starting_with_an_empty_list_ten_integers_descending():
    items_to_insert = [ 31, 5, 75, 3, 25, 45, 80, 4, 93, 7 ]
    item_list = []
    for item in items_to_insert:
        insert_into(item_list, item, ascending=False)
    assert item_list == [93, 80, 75, 45, 31, 25, 7, 5, 4, 3], "Successfully inserted in descending order ten integers into a list"

def test_insert_into_starting_with_an_empty_list_ten_strings_ascending():
    items_to_insert = [
        'Harriet Tubman',
        'Mansa Musa',
        'Frida Kahlo',
        'Genghis Khan',
        'Leonardo da Vinci',
        'Marie Curie',
        'Rani Lakshmibai',
        'Tȟašúŋke Witkó',
        'Cleopatra VII',
        'Queen Seondeok of Silla',
    ]
    item_list = []
    for item in items_to_insert:
        insert_into(item_list, item)
    assert item_list == [
                           'Cleopatra VII',
                           'Frida Kahlo',
                           'Genghis Khan',
                           'Harriet Tubman',
                           'Leonardo da Vinci',
                           'Mansa Musa',
                           'Marie Curie',
                           'Queen Seondeok of Silla',
                           'Rani Lakshmibai',
                           'Tȟašúŋke Witkó'
                         ], (
            "Successfully inserted in ascending order ten strings into a list" )

#if __name__ == '__main__':
#   test_insert_into_starting_with_an_empty_list_ten_items_ascending()
#    test_insert_into_starting_with_an_empty_list_ten_items_descending()
