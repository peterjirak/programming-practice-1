class ListSubsetGenerator:
    def __init__(self, item_list):
        self.item_list = item_list
        item_count = len(item_list)
        subset_count = ( 1 << item_count ) - 1
        subset_bitmask = 1
        self.item_count = item_count
        self.subset_count = subset_count
        self.subset_bitmask = subset_bitmask
    
    def get_next_subset(self):
        if self.subset_bitmask > self.subset_count:
            return None
        subset = [self.item_list[j] for j in range(len(self.item_list)) if self.subset_bitmask & (1 << j) ]
        self.subset_bitmask += 1
        return subset

