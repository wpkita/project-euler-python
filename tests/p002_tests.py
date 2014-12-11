from nose.tools import *
from p002.solution import *


def test_fibonacci_sequence():
    fib_numbers_up_to_10 = fib_with_max_num(10)

    assert_equal(fib_numbers_up_to_10, [1, 2, 3, 5, 8])
