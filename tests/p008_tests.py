from nose.tools import *
from p008.solution import *


def test_product():
    assert_equal(product([1, 2, 3, 4]), 24)
    assert_equal(product([5, 6, 7, 3]), 630)
    assert_equal(product([5, 8, 0, 3]), 0)


def test_get_highest_adjacent_product():
    assert_equal(get_highest_adjacent_product('123456789', 4), 3024)
    assert_equal(get_highest_adjacent_product('197543682', 4), 1260)
