"""
shift_right(item_list, index)

ARGUMENTS
1. item_list - a list
2. index - The index starting at which all items will be shifted one space to
   the right.

RETURNS
None

DESCRIPTION
Takes a list and an index and shifts all elements one space to the right starting
at the specified index.

None is assigned to the list at the specified index.
"""
def shift_right(item_list, index):
    item_list.append(None)
    for i in range(len(item_list) - 1, index, -1):
        item_list[i] = item_list[i - 1]
    item_list[index] = None
    return

"""
insert_into(item_list, item, left, right, ascending)

ARGUMENTS
1. item_list - a list of sorted items, possibly empty
2. item - an item to add into the list
3. left - this function uses a binary search algorithm to find where to insert
          the item into the list. left is the left-most index of the list in
          which to insert the item. When the algorithm starts, left is zero and
          right is len(item_list) - 1. left and right are reduced by half until
          the insertion spot of item is found through recursion.
4. right - this function uses a binary search algorithm to find where to insert
           the item into the list. right is the right-most index of the list in
           which to insert the item. When the algorithm starts, left is zero and
           right is len(item_list) - 1. left and right are reduced by half until
           the insertion spot of item is found through recursion.
5. ascending - True if the list is sorted in ascending order. False if it is
               sorted iin descending order.

RETURNS
None

DESCRIPTION
Takes in a sorted list (possibly empty), an item to add, left (the left-most
index in which to place item - zero initially), right (the right-most index in
which to place the item - len(item_list) - 1 initially), ascending (True or False).
It recursively calls itself until it finds the place in which to insert the item,
it then inserts the item and returns. On each recursive call the difference between
right - left is reduced by half.
"""
def insert_into(item_list, item, left=None, right=None, ascending=True):
    left = 0 if left is None else left
    right = max(len(item_list) - 1, 0) if right is None else right
    if left > right:
        raise ValueError(f'Bad invocation of insert_into - left == {left}, ' +
                         f'right == {right} - left cannot be greater than right.')
    elif left == right:
        if len(item_list) == 0:
            item_list.append(item)
            return
        if ascending:
            if item >= item_list[right]:
                if len(item_list) - 1 == right:
                    item_list.append(item)
                    return
                else:
                    shift_right(item_list, right + 1)
                    item_list[right + 1] = item
                    return
            else:
                shift_right(item_list, right)
                item_list[right] = item
                return
        else:
            if item <= item_list[right]:
                if len(item_list) - 1 == right:
                    item_list.append(item)
                    return
                else:
                    shift_right(item_list, right + 1)
                    item_list[right + 1] = item
                    return
            else:
                shift_right(item_list, right)
                item_list[right] = item
                return
    elif right - left == 1:
        if ascending:
            if item <= item_list[left]:
                shift_right(item_list, left)
                item_list[left] = item
                return
            elif item >= item_list[right]:
                if right == len(item_list) - 1:
                    item_list.append(item)
                    return
                else:
                    shift_right(item_list, right + 1)
                    item_list[right + 1] = item
                    return
            else:
                shift_right(item_list, right)
                item_list[right] = item
                return
        else:
            if item >= item_list[left]:
                shift_right(item_list, left)
                item_list[left] = item
                return
            elif item <= item_list[right]:
                if right == len(item_list) - 1:
                    item_list.append(item)
                    return
                else:
                    shift_right(item_list, right + 1)
                    item_list[right + 1] = item
                    return
            else:
                shift_right(item_list, right)
                item_list[right] = item
                return

    if ascending:
        if item <= item_list[left]:
            insert_into(item_list, item, left, left, ascending)
            return
        elif item >= item_list[right]:
            insert_into(item_list, item, right, right, ascending)
            return
        mid = ( left + right ) // 2
        if item == item_list[mid]:
            insert_into(item_list, item, mid, mid, ascending)
            return
        elif item < item_list[mid]:
            insert_into(item_list, item, left, mid, ascending)
            return
        else:
            insert_into(item_list, item, mid, right, ascending)
            return
    else:
        if item >= item_list[left]:
            insert_into(item_list, item, left, left, ascending)
            return
        elif item <= item_list[right]:
            insert_into(item_list, item, right, right, ascending)
            return
        mid = ( left + right ) // 2
        if item == item_list[mid]:
            insert_into(item_list, item, mid, mid, ascending)
            return
        elif item > item_list[mid]:
            insert_into(item_list, item, left, mid, ascending)
            return
        else:
            insert_into(item_list, item, mid, right, ascending)
            return
