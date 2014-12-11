def sum_of_squares(up_to):
    return sum([i**2 for i in range(1, up_to + 1)])


def square_of_sum(up_to):
    return sum(range(1, up_to + 1)) ** 2

if __name__ == '__main__':
    VALUE = 100

    print('Sum square difference: ', square_of_sum(VALUE) - sum_of_squares(VALUE))
