from nose.tools import *
from p002.solution import *


def test_fibonacci_sequence():
    fib_numbers_up_to_10 = fibonacci_numbers_up_to(10)

    assert_equal(fib_numbers_up_to_10, [1, 2, 3, 5, 8])


def test_sum_of_evens():
    assert_equal(sum_of_evens([1, 2, 3, 4]), 6)
    assert_equal(sum_of_evens([7, 13, 19]), 0)
    assert_equal(sum_of_evens([]), 0)