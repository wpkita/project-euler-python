from functools import reduce
from operator import mul


def product(lst):
    return reduce(mul, lst)


def get_highest_product_in_grid(grid, group_length):
    # Assumes square grid
    dimension = len(grid)

    if group_length > dimension:
        return -1

    max_product = 0

    # Iterate over rows
    for row in grid:
        for col in range(dimension - (group_length - 1)):
            lst = row[col:col+group_length]
            max_product = max(max_product, product(lst))

    # Iterate over columns
    for row in range(dimension - (group_length - 1)):
        for col in range(dimension):
            lst = []
            for offset in range(group_length):
                lst.append(grid[row + offset][col])
            max_product = max(max_product, product(lst))

    # Iterate over diagonals
    for row in range(dimension - (group_length - 1)):
        for col in range(dimension - (group_length - 1)):
            lst = []
            for offset in range(group_length):
                lst.append(grid[row + offset][col + offset])
            max_product = max(max_product, product(lst))

    return max_product

if __name__ == '__main__':
    number_grid = []

    with open('number-grid.txt', 'r') as number_grid_file:
        for line in number_grid_file:
            number_grid.append([int(number) for number in line.strip().split()])

    print(get_highest_product_in_grid(number_grid, 4))
