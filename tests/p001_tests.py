from nose.tools import *
from p001.solution import *


def test_loop_version():
    assert_equal(get_sum_of_multiples_using_loop(10), 23)
