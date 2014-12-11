"""
Title
======
Even Fibonacci numbers

Problem
=======
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""


def fib_with_max_num(max_num):
    first = 1
    second = 2

    if max_num == 1:
        return [first]

    if max_num == 2:
        return [first, second]

    seq = [first, second]
    while True:
        next_num = first + second
        first = second
        second = next_num
        if next_num > max_num:
            break
        seq.append(next_num)

    return seq
