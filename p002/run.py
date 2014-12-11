from solution import *

fibs_not_exceeding_four_million = fib_with_max_num(4000000)
sum_of_even_fibs_not_exceeding_four_million = 0
for i in fibs_not_exceeding_four_million:
    if i % 2 == 0:
        sum_of_even_fibs_not_exceeding_four_million += i

print('Sum of even Fibonacci numbers not exceeding four million: ', sum_of_even_fibs_not_exceeding_four_million)
