def _get_next(indices, lengths, *lists):
    min_item = None
    list_index = None

    for i in range(len(lists)):
        length = lengths[i]
        index = indices[i]
        if index >= length:
            continue
        elif min_item is None or lists[i][index] < min_item:
            min_item = lists[i][index]
            list_index = i
    
    if list_index is not None:
        indices[list_index] += 1

    return min_item

def merge_sorted_lists(*lists):
    list_count = len(lists)
    lengths = [None] * list_count
    for i in range(len(lists)):
        lengths[i] = len(lists[i])
    indices = [0] * list_count
    item_count = sum(lengths)
    merged = [None] * item_count
    m = 0
    
    next_item = _get_next(indices, lengths, *lists)
    while next_item is not None:
        merged[m] = next_item
        m += 1
        next_item = _get_next(indices, lengths, *lists)
    
    return merged
