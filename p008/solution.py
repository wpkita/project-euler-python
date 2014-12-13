from functools import reduce
from operator import mul


def product(factors):
    return reduce(mul, factors)


def get_highest_adjacent_product(value, number_of_adjacencies):
    highest_product_so_far = 0

    for i in range(len(value) - (number_of_adjacencies - 1)):
        current_product = product([int(c) for c in value[i:i + number_of_adjacencies]])
        highest_product_so_far = max(highest_product_so_far, current_product)

    return highest_product_so_far

if __name__ == '__main__':
    big_number_str = ''
    with open('big-number.txt', 'r') as big_number_file:
        big_number_str = big_number_file.read().replace('\n', '')

    print(get_highest_adjacent_product(big_number_str, 13))
