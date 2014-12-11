"""
Title
=====
Largest palindrome product

Problem
=======
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def is_number_a_palindrome(number):
    as_string = str(number)

    return as_string == as_string[::-1]
