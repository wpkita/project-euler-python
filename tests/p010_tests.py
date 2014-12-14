from nose.tools import *
from p010.solution import *


def test_generate_primes_up_to():
    assert_equal(generate_primes_up_to(5), [2, 3, 5])
    assert_equal(generate_primes_up_to(10), [2, 3, 5, 7])
    assert_equal(generate_primes_up_to(20), [2, 3, 5, 7, 11, 13, 17, 19])
