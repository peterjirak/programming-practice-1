from list_sort_in_place import sort_in_place

def test_sort_in_place_ten_integers_ascending():
    items = [ 31, 5, 75, 3, 25, 45, 80, 4, 93, 7 ]
    sort_in_place(items, ascending=True)
    assert items == [3, 4, 5, 7, 25, 31, 45, 75, 80, 93], "Successfully sorted in ascending order a list of ten integers"

def test_sort_in_place_ten_integers_descending():
    items = [ 31, 5, 75, 3, 25, 45, 80, 4, 93, 7 ]
    sort_in_place(items, ascending=False)
    assert items == [93, 80, 75, 45, 31, 25, 7, 5, 4, 3], "Successfully sorted in descending order a list of ten integers"

def test_sort_in_place_ten_strings_ascending():
    items = [
        'Harriet Tubman',
        'Mansa Musa',
        'Frida Kahlo',
        'Genghis Khan',
        'Leonardo da Vinci',
        'Marie Curie',
        'Rani Lakshmibai',
        'Tȟašúŋke Witkó',
        'Cleopatra VII',
        'Queen Seondeok of Silla'
    ]
    sort_in_place(items, ascending=True)
    assert items == [
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
            "Successfully sorted in ascending order a list of ten strings" )

def test_sort_in_place_ten_strings_descending():
    items = [
        'Harriet Tubman',
        'Mansa Musa',
        'Frida Kahlo',
        'Genghis Khan',
        'Leonardo da Vinci',
        'Marie Curie',
        'Rani Lakshmibai',
        'Tȟašúŋke Witkó',
        'Cleopatra VII',
        'Queen Seondeok of Silla'
    ]
    sort_in_place(items, ascending=False)
    assert items == [
                        'Tȟašúŋke Witkó',
                        'Rani Lakshmibai',
                        'Queen Seondeok of Silla',
                        'Marie Curie',
                        'Mansa Musa',
                        'Leonardo da Vinci',
                        'Harriet Tubman',
                        'Genghis Khan',
                        'Frida Kahlo',
                        'Cleopatra VII'
                    ], (
            "Successfully sorted in descending order a list of ten strings" )


# if __name__ == '__main__':
#     test_sort_in_place_ten_integers_descending()
