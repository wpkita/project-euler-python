from solution import *

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
