from list_merge_two_sorted_lists import is_ascending, is_descending

def _get_next(indices, lengths, *lists, ascending=True):
    next_item = None
    list_index = None

    for i in range(len(lists)):
        length = lengths[i]
        index = indices[i]
        if index >= length:
            continue
        elif ascending:
            if next_item is None or lists[i][index] < next_item:
                next_item = lists[i][index]
                list_index = i
        else:
            if next_item is None or lists[i][index] > next_item:
                next_item = lists[i][index]
                list_index = i
    
    if list_index is not None:
        indices[list_index] += 1

    return next_item

def merge_sorted_lists(*lists):
    are_ascending = None
    are_descending = None
    for i in range(len(lists)):
        l = lists[i]
        asc = is_ascending(l)
        desc = is_descending(l)
        if not asc and not desc:
            raise ValueError(f'The list in position {i} is neither ascending nor descending')
        elif asc:
            if are_descending:
                raise ValueError(f'The lists in positions 0 - {i - 1} ' +
                                 'are descending while the list at position ' +
                                 f'{i} is ascending.')
            elif are_descending is None and are_ascending is None:
                are_ascending = True
                are_descending = not are_ascending
        else:
            if are_ascending:
                raise ValueError(f'The lists in positions 0 - {i - 1} ' +
                                 'are ascending while the list at position ' +
                                 f'{i} is descending.')
            elif are_descending is None and are_ascending is None:
                are_descending = True
                are_ascending = not are_descending

    list_count = len(lists)
    lengths = [None] * list_count
    for i in range(len(lists)):
        lengths[i] = len(lists[i])
    indices = [0] * list_count
    item_count = sum(lengths)
    merged = [None] * item_count
    m = 0
    
    next_item = _get_next(indices, lengths, *lists, ascending=are_ascending)
    while next_item is not None:
        merged[m] = next_item
        m += 1
        next_item = _get_next(indices, lengths, *lists, ascending=are_ascending)
    
    return merged
