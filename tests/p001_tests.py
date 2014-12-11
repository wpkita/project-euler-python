from nose.tools import *
from p001.solution import *


def test_loop_version():
    sum_of_multiples_for_10 = get_sum_of_multiples_using_loop(10)

    assert_equal(sum_of_multiples_for_10, 23)


def test_list_comprehension_version():
    sum_of_multiples_for_10 = get_sum_of_multiples_using_list_comprehension(10)

    assert_equal(sum_of_multiples_for_10, 23)
