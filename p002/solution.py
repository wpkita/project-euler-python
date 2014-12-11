def fibonacci_numbers_up_to(max_num):
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


def sum_of_evens(numbers):
    return sum(i for i in numbers if i % 2 == 0)

if __name__ == '__main__':
    fibs_not_exceeding_four_million = fibonacci_numbers_up_to(4000000)
    sum_of_even_fibs_not_exceeding_four_million = sum_of_evens(fibs_not_exceeding_four_million)

    print('Sum of even Fibonacci numbers not exceeding four million: ', sum_of_even_fibs_not_exceeding_four_million)
