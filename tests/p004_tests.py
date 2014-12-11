from nose.tools import *
from p004.solution import *


def test_is_number_a_palindrome():
    assert_true(is_number_a_palindrome(1))
    assert_true(is_number_a_palindrome(101))
    assert_true(is_number_a_palindrome(1111))
    assert_true(is_number_a_palindrome(990060099))

    assert_false(is_number_a_palindrome(12))
    assert_false(is_number_a_palindrome(133))
    assert_false(is_number_a_palindrome(45673820))
