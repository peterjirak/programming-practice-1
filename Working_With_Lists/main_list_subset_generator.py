from list_subset_generator import ListSubsetGenerator

if __name__ == '__main__':
    item_str = input('Enter a space delimited set of items: ')
    items = item_str.split()
    subset_generator = ListSubsetGenerator(items)
    subset = subset_generator.get_next_subset()
    i = 1
    while (subset):
        print(f"{i}: {subset}")
        i += 1
        subset = subset_generator.get_next_subset()
    