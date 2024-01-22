from list_subsets_2 import subset_sums_to_zero

if __name__ == "__main__":
    integer_list_str = input('Enter a space separated list of integers: ')
    integer_list = integer_list_str.split()
    integer_list = list(map(int, integer_list))
    result = subset_sums_to_zero(integer_list)
    if len(result) == 0:
        print('The list contained no subset that summed to zero')
    else:
        print(f"{' + '.join(list(map(str, result)))} == 0")
