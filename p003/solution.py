"""
Title
======
Largest prime factor

Problem
=======
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""


def get_factors_rec(number, factors):
    for i in range(2, number // 2):
        if number % i == 0:
            factors.append(i)
            get_factors_rec(number // i, factors)
            return

    # If we got this far, then this is a prime factor
    factors.append(number)


def get_factors(number):
    factors = []

    get_factors_rec(number, factors)

    return factors


def get_largest_prime_factor(number):
    factors = get_factors(number)

    return max(factors)


largest_prime_factor = get_largest_prime_factor(600851475143)

print('Largest prime factor: ', largest_prime_factor)
