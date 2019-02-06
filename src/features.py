import numpy as np
from src.auxiliary_methods import *
from src.sort import *


# param array : np.array
def fill_features(array):

    features = {}

    calculate_inversions(features, array)
    calculate_digits(features, array)
    calculate_digits_base_2(features, array)
    calculate_custom_features(features, array)
    calculate_duplicates(features, array)

    return features


def calculate_inversions(features, array):
    
    if array.size == 0 or array.size == 1:
        features['inversion'] = 0
        features['consecutive_inversion'] = 0
        return
    inv = 0
    for i in range(array.size - 1):
        for j in range(i):
            if array[j] > array[i]:
                inv = inv + 1

    cons_inv = 0
    for i in range(array.size - 1):
        if array[i] > array[i+1]:
            cons_inv = cons_inv + 1

    possible_max = ((array.size - 1) * array.size) / 2

    # (number of inversions) / (possible maximum inversions)
    features['inversion'] = inv / possible_max
    # (number of consecutive inversions) / (array length)
    features['consecutive_inversion'] = cons_inv / array.size


def calculate_digits(features, array):
    arr = []
    for num in array:
        arr.append(count_digits(num))

    digits = np.array(arr)

    # (maximum of digits)
    features['max_digit'] = digits.max()
    # (minimum of digits)
    features['min_digit'] = digits.min()
    # (expectation of digits)
    features['expectation_of_digits'] = digits.mean()
    # (std. deviation of digits)
    features['deviation_of_digits'] = digits.std()


def calculate_digits_base_2(features, array):
    arr = []
    for num in array:
        arr.append(count_digits_base_2(num))

    digits = np.array(arr)

    # (maximum of digits)
    features['max_digit_base_2'] = digits.max()
    # (minimum of digits)
    features['min_digit_base_2'] = digits.min()
    # (expectation of digits)
    features['expectation_of_digits_base_2'] = digits.mean()
    # (std. deviation of digits)
    features['deviation_of_digits_base_2'] = digits.std()


def calculate_custom_features(features, array):
    # array length
    features['length'] = array.size


def calculate_duplicates(features, array):
    duplicates = {}
    for num in array:
        if str(num) in duplicates:
            duplicates[str(num)] = duplicates[str(num)] + 1
        else:
            duplicates[str(num)] = 1

    arr = []
    for dup in duplicates:
        arr.append(duplicates[dup])

    dups = np.array(arr)

    # (maximum occurrence of a duplicate) / (array length)
    features['max_duplicate'] = float(dups.max()) / array.size
    # (minimum occurrence of a duplicate) / (array length)
    features['min_duplicate'] = float(dups.min()) / array.size
    # (expectation of occurrences of a duplicate) / (array length)
    features['expectation_of_duplicates'] = dups.mean() / array.size
    # (std. deviation of occurrences of a duplicate) / (array length)
    features['deviation_of_duplicates'] = dups.std() / array.size

