"""
is_ascending(item_list)

ARGUMENTS
1. item_list

RETURNS
True if and only if item_list is ordered in ascending order
"""
def is_ascending(item_list):
    for i in range(len(item_list) - 1):
        if item_list[i] > item_list[i + 1]:
            return False
    return True

"""
is_descending(item_list)

ARGUMENTS
1. item_list

RETURNS
True if and only if item_list is ordered in descending order
"""
def is_descending(item_list):
    for i in range(len(item_list) - 1):
        if item_list[i] < item_list[i + 1]:
            return False
    return True

"""
list_merge_two_sorted_lists(item_list1, item_list2)

ARGUMENTS
1. item_list1 - A list of items - sorted, ascending
2. item_list2 - A list of items - sorted, ascending

RETURNS
A list containing the rtwo lists merged in ascending order

DESCRIPTION
Takes in two sorted lists (ascending) and returns a list containing the two lists,
merged, sorted (ascending)
"""
def list_merge_two_sorted_lists(item_list1, item_list2):
    merged_list = []
    i1 = 0
    i2 = 0
    len1 = len(item_list1)
    len2 = len(item_list2)
    if len1 == 0 and len2 == 0:
        return []
    ascending = None
    ascending1 = is_ascending(item_list1)
    ascending2 = is_ascending(item_list2)
    descending1 = is_descending(item_list1)
    descending2 = is_descending(item_list2)
    if len1 == 0:
        if ascending2:
            ascending = True
        elif descending2:
            ascending = False
        else:
            raise ValueError('item_list2 is not sorted')
    elif len2 == 0:
        if ascending1:
            ascending = True
        elif descending1:
            ascending = False
        else:
            raise ValueError('item_list1 is not sorted')
    elif ascending1:
        if not ascending2:
            raise ValueError('item_list1 is ascending but item_list2 is not ascending')
        else:
            ascending = True
    elif descending1:
        if not descending2:
            raise ValueError('item_list1 is descending but item_list2 is not descending')
        else:
            ascending = False
    elif not descending2:
        raise ValueError('argument lists are not sorted')
    else:
        raise ValueError('item_list1 is not sorted')

    while i1 < len1 and i2 < len2:
        if i1 < len1 and i2 < len2:
            if ascending:
                if item_list1[i1] <= item_list2[i2]:
                    merged_list.append(item_list1[i1])
                    i1 += 1
                else:
                    merged_list.append(item_list2[i2])
                    i2 += 1
            else:
                if item_list1[i1] >= item_list2[i2]:
                    merged_list.append(item_list1[i1])
                    i1 += 1
                else:
                    merged_list.append(item_list2[i2])
                    i2 += 1
    for j in range(i1, len1):
        merged_list.append(item_list1[j])
    for j in range(i2, len2):
        merged_list.append(item_list2[j])
    return merged_list