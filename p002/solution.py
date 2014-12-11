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
