from solution import *

largest_palindrome_product = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i * j
        if is_number_a_palindrome(product) and product > largest_palindrome_product:
            largest_palindrome_product = product

print('Largest palindrome product: ', largest_palindrome_product)
