"""
Title
=====
Smallest multiple

Problem
=======
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def is_divisible_by_consecutive_numbers(number, minimum, maximum):
    for i in range(minimum, maximum + 1):
        if number % i != 0:
            return False

    return True

MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 20

have_not_found_a_match = True
current_number = MAXIMUM_NUMBER

while have_not_found_a_match:
    if is_divisible_by_consecutive_numbers(current_number, MINIMUM_NUMBER + 1, MAXIMUM_NUMBER):
        have_not_found_a_match = False
    else:
        current_number += MAXIMUM_NUMBER

print('Smallest multiple: ', current_number)
