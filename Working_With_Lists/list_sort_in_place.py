"""
_find_insertion_index(list_items, item, left, right, ascending=True)

ARGUMENTS
1. list_items - A list of items
2. item - An item to add
3. left - The left most index of the range to search for the index at which
          the item should be inserted.
4. right - The right most index of the range to search for the index at which
           the item should be inserted.
5. ascending - Boolean flag. If true, list is in ascending order. If false, list
               is in descending order.

RETURNS
The index (whose value will be in the range [left, right + 1]) of the cell in
the list_items array where the item should be inserted.

DESCRIPTION
This is a helper function that is invoked from the function sort_in_place. It
takes as input a list_items, an item to insert, left (the left-most index of the
range of cells where the item could be inserted), right (the right-most index of
the range of cells where the item could be inserted), and ascending (a boolean
flag indicating whether it is an scending or descending list).

_find_insertion_index uses the bisection method to recursively find the index in
list_items where item should be inserted.
"""
def _find_insertion_index(list_items, item, left, right, ascending=True):
    if left > right:
        raise ValueError(f'Bad invocation of insert_into - left == {left}, ' +
                         f'right == {right} - left cannot be greater than right.')
    elif right - left <= 1:
        if ascending:
            if item <= list_items[left]:
                return left
            elif item >= list_items[right]:
                return right + 1
            else:
                return right
        else:
            if item >= list_items[left]:
                return left
            elif item <= list_items[right]:
                return right + 1
            else:
                return right
    else:
        if ascending:
            if item <= list_items[left]:
                return left
            elif item >= list_items[right]:
                return right + 1
            else:
                mid = ( left + right ) // 2
                if item == list_items[mid]:
                    return mid
                elif item < list_items[mid]:
                    return _find_insertion_index(list_items, item, left, mid, ascending)
                else:
                    return _find_insertion_index(list_items, item, mid, right, ascending)
        else:
            if item >= list_items[left]:
                return left
            elif item <= list_items[right]:
                return right + 1
            else:
                mid = ( left + right ) // 2
                if item == list_items[mid]:
                    return mid
                elif item > list_items[mid]:
                    return _find_insertion_index(list_items, item, left, mid, ascending)
                else:
                    return _find_insertion_index(list_items, item, mid, right, ascending)

"""
sort_in_place(list_items, ascending=True)

Uses the bisection method (by invoking the _find_insertion_index helper function)
to sort list_items in place without constructing and returning a new array of items.
"""
def sort_in_place(list_items, ascending=True):
    for sorted in range(0, len(list_items) - 1):
        next_item = list_items[sorted + 1]
        insert_at = _find_insertion_index(list_items, next_item, 0, sorted, ascending)
        if insert_at == sorted + 1:
            continue
        for i in range(sorted + 1, insert_at, -1):
            list_items[i] = list_items[i - 1]
        list_items[insert_at] = next_item
    return
