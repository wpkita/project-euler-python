from nose.tools import *
from p011.solution import *


def test_get_highest_product_in_grid():
    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert_equal(get_highest_product_in_grid(grid, 2), 72)

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert_equal(get_highest_product_in_grid(grid, 3), 504)

    grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert_equal(get_highest_product_in_grid(grid, 4), -1)
