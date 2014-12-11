from nose.tools import *
from p006.solution import *


def test_naive_sum_of_squares():
    assert_equal(naive_sum_of_squares(10), 385)


def test_pyramidal_sum_of_squares():
    assert_equal(pyramidal_sum_of_squares(10), 385)


def test_square_of_sums():
    square_of_sums_up_to_10 = square_of_sum(10)

    assert_equal(square_of_sums_up_to_10, 3025)
