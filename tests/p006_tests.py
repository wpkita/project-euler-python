from nose.tools import *
from p006.solution import *


def test_naive_sum_of_squares():
    assert_equal(naive_sum_of_squares(10), 385)


def test_pyramidal_sum_of_squares():
    assert_equal(pyramidal_sum_of_squares(10), 385)


def test_naive_square_of_sum():
    assert_equal(naive_square_of_sum(10), 3025)


def test_arithmetic_series_square_of_sum():
    assert_equal(arithmetic_series_square_of_sum(10), 3025)
