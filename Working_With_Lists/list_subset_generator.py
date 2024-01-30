"""
class ListSubsetGenerator

DESCRIPTION
An instance of ListSubsetGenerator may be used to construct all of the subsets
of a list.

A subset of a list is a list that contains all or some of the elements
of the list. For example take the list ['a', 'b', 'c'], ['a'] is a subset of
that list, ['b'] is a subset of that list, ['c'] is a subset of that list, so is
['a', 'b'], as is ['a', 'c'], as is ['a', 'b'], ['b', 'c'] is also a subset, and
the list itself is a subset ['a', 'b', 'c']. However, ['a', 'd'] is not a subset
of the original list since 'd' is not in the original list.

The empty list [] is considered to be a subset of all lists, but our
ListSubsetGenerator omits the empty list. There are 2**n - 1 subsets of any
list where n is the number of items in the list that includes the empty list.
There are 2**n - 2 if one excludes the empty list.

EXAMPLE CODE
# Create a ListSubsetGenerator
characters = [ 'Morrigan Crow', 'Jupiter North', 'Fenestra']
list_subset_generator = ListSubsetGenerator(characters)

i = 1
# Get the first subset by invoking the get_next_subset on ListSubsetGenerator
subset = list_subset_generator.get_next_subset()
while subset:
        print(f"{i}: {subset}")
        i += 1
        # Get the next subset:
        subset = subset_generator.get_next_subset()

---------------------------------------------------------------------
% Output
% 1: ['Morrigan Crow']
% 2: ['Jupiter North']
% 3: ['Morrigan Crow', 'Jupiter North']
% 4: ['Fenestra']
% 5: ['Morrigan_Crow', 'Fenestra']
% 6: ['Jupiter_North', 'Fenestra']
% 7: ['Morrigan Crow', 'Jupiter North', 'Fenestra']

"""

class ListSubsetGenerator:
    """
    Constructor: ListSubsetGenerator(item_list)

    Takes in an argument list and returns an instance of ListSubsetGenerator.
    One can construct each subset of the original list by repeatedly 
    """
    def __init__(self, item_list):
        self.item_list = item_list
        item_count = len(item_list)
        subset_count = ( 1 << item_count ) - 1
        subset_bitmask = 1
        self.item_count = item_count
        self.subset_count = subset_count
        self.subset_bitmask = subset_bitmask
    
    """
    Member method: get_next_subset()

    Returns a list containing the next subset of the original list. The empty
    list is considered a subset of all lists and is never returned by
    get_next_subset. None is returned once all subsets have been returned.
    The last subset returned is the list of items itself. The original list is
    itself a subset based on the definition of a subset.
    """
    def get_next_subset(self):
        if self.subset_bitmask > self.subset_count:
            return None
        subset = [self.item_list[j] for j in range(len(self.item_list)) if self.subset_bitmask & (1 << j) ]
        self.subset_bitmask += 1
        return subset

