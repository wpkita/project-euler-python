def get_sum_of_multiples_using_loop(maximum):
    sum_of_multiples = 0

    for i in range(1, maximum):
        if i % 5 == 0 or i % 3 == 0:
            sum_of_multiples += i

    return sum_of_multiples


def get_sum_of_multiples_using_list_comprehension(maximum):
    return sum([i for i in range(1, maximum) if i % 5 == 0 or i % 3 == 0])
