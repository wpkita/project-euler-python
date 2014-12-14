from functools import reduce
from operator import mul


def get_pythagorean_triple_summing_to(pythagorean_sum):
    for m in range(2, pythagorean_sum):
        for n in range(1, m):
            a = m ** 2 - n ** 2
            b = 2 * m * n
            c = m ** 2 + n ** 2

            if a + b + c == pythagorean_sum:
                return a, b, c


if __name__ == '__main__':
    pythagorean_triple = get_pythagorean_triple_summing_to(1000)
    product_of_triple = reduce(mul, pythagorean_triple)

    print(product_of_triple)
