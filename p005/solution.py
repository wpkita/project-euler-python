def is_divisible_by_consecutive_numbers(number, minimum, maximum):
    for i in range(minimum, maximum + 1):
        if number % i != 0:
            return False

    return True
