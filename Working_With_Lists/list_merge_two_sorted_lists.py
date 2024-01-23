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
    while i1 < len1 and i2 < len2:
        if i1 < len1 and i2 < len2:
            if item_list1[i1] <= item_list2[i2]:
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
