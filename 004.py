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

largest_palindrome_product = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_number_a_palindrome(product) and product > largest_palindrome_product:
            largest_palindrome_product = product

print('Largest palindrome product: ', largest_palindrome_product)
