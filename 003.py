"""
Title
======
Largest prime factor

Problem
=======
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import floor


def get_largest_prime_factor(number):
    # Begin at the halfway point, since no factors will be greater than that
    mid = floor(number / 2)

    # Recursively traverse factor tree
    for i in range(mid, 1, -1):
        if number % i == 0:
            return get_largest_prime_factor(i)

    return number

largest_prime_factor = get_largest_prime_factor(600851475143)

print('Largest prime factor: ', largest_prime_factor)
