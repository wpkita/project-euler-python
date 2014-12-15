from nose.tools import *
from p007.solution import *


def test_is_prime():
    assert_true(is_prime(2))
    assert_true(is_prime(3))
    assert_false(is_prime(4))
    assert_true(is_prime(5))
    assert_false(is_prime(6))
    assert_false(is_prime(9))


def test_generate_nth_prime():
    assert_equal(generate_nth_prime(1), 2)
    assert_equal(generate_nth_prime(2), 3)
    assert_equal(generate_nth_prime(6), 13)
