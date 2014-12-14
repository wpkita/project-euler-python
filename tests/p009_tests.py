from nose.tools import *
from p009.solution import *


def test_get_pythagorean_triple_summing_to():
    assert_equal(get_pythagorean_triple_summing_to(12), (3, 4, 5))
    assert_equal(get_pythagorean_triple_summing_to(30), (5, 12, 13))
