from listtools import insert_into

def _get_subset_for_bitmask(integer_list, bitmask):
    subset = [integer_list[j] for j in range(len(integer_list)) if (bitmask & (1 << j)) > 0]
    return subset

"""
Create a function that takes in a list of integers and returns any subset that
adds up to zero
"""
def subset_sums_to_zero(integer_list):
    positive_list = []
    positive_set = set()
    negative_list = []
    negative_set = set()
    for integer in integer_list:
        if integer == 0:
            return [0]
        elif integer > 0:
            insert_into(positive_list, integer)
            positive_set.add(integer)
            if integer in negative_set:
                return [integer, integer * -1]
        else:
            insert_into(negative_list, abs(integer))
            negative_set.add(abs(integer))
            if abs(integer) in positive_set:
                return [integer, integer * -1]
    if len(positive_list) == 0 or len(negative_list) == 0:
        return []
    search_list_type = None
    search = None
    compliment = None
    if len(positive_list) < len(negative_list):
        search_list_type = 1
        search = positive_list
        compliment = negative_list
    else:
        search_list_type = -1
        search = negative_list
        compliment = positive_list

    for i in range(1, 1 << len(search)):
        subset = _get_subset_for_bitmask(search, i)
        subset_total = sum(subset)
        candidate_compliment_values = []
        for num in compliment:
            if num == subset_total:
                solution = [val * search_list_type for val in subset]
                solution.append(num * search_list_type * -1)
                return solution
            elif num < subset_total:
                candidate_compliment_values.append(num)
            else:
                break
        if len(candidate_compliment_values) == 0:
            continue
        for j in range(1, 1 << len(candidate_compliment_values)):
            compliment_subset = _get_subset_for_bitmask(candidate_compliment_values, j)
            if len(subset) == 1 and len(compliment_subset) == 1:
                continue
            compliment_subset_total = sum(compliment_subset)
            if subset_total == compliment_subset_total:
                first_half = [num * search_list_type for num in subset]
                second_half = [num * search_list_type * -1 for num in compliment_subset]
                return first_half + second_half
    return []
