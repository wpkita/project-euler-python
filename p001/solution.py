"""
Title
======
Multiples of 3 and 5

Problem
=======
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_sum_of_multiples_using_loop(maximum):
    sum_of_multiples = 0

    for i in range(1, maximum):
        if i % 5 == 0 or i % 3 == 0:
            sum_of_multiples += i

    return sum_of_multiples
