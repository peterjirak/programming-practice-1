from itertools import combinations

"""
Create a function that takes in a list of integers and returns any subset that
adds up to zero
"""
def subset_sums_to_zero_v1(integer_list):
    if 0 in integer_list:
        return [0]
    
    for i in range(2, len(integer_list)):
        for subset in combinations(integer_list, i):
            total = sum(subset)
            if total == 0:
                return list(subset)
    return []

def subset_sums_to_zero_v2(integer_list):
    if 0 in integer_list:
        return [0]
    
    for i in range(3, 1 << len(integer_list)):
        subset = [integer_list[j] for j in range(len(integer_list)) if (i & (1 << j)) > 0]
        if len(subset) == 1:
            continue
        total = sum(subset)
        if total == 0:
            return subset
    return []
