def naive_sum_of_squares(up_to):
    return sum([i**2 for i in range(1, up_to + 1)])


# Based on square pyramidal number formula
def pyramidal_sum_of_squares(up_to):
    return (2 * up_to ** 3 + 3 * up_to ** 2 + up_to) / 6


def naive_square_of_sum(up_to):
    return sum(range(1, up_to + 1)) ** 2


def arithmetic_series_square_of_sum(up_to):
    return (up_to * (up_to + 1) / 2) ** 2

if __name__ == '__main__':
    VALUE = 100

    print('Sum square difference: ', arithmetic_series_square_of_sum(VALUE) - pyramidal_sum_of_squares(VALUE))
