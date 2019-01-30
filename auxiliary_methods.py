def count_digits(number):
    return 0 if int(number) == 0 else 1 + count_digits(number / 10)


def count_digits_base_2(number):
    return 0 if int(number) == 0 else 1 + count_digits_base_2(number / 2)
