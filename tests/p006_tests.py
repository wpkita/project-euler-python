from nose.tools import *
from p006.solution import *


def test_sum_of_squares():
    sum_of_squares_up_to_10 = sum_of_squares(10)

    assert_equal(sum_of_squares_up_to_10, 385)


def test_square_of_sums():
    square_of_sums_up_to_10 = square_of_sums(10)

    assert_equal(square_of_sums_up_to_10, 3025)
