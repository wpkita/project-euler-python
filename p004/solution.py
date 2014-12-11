def is_number_a_palindrome(number):
    as_string = str(number)

    return as_string == as_string[::-1]
