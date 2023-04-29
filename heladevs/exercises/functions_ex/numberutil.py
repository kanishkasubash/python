""" Module for basic number operations in the list
    - Total
    - Average
    - Minimum
    - Maximum
"""
def total(numbers: list) -> int:
    """Calculate the sum of the given numbers in the list"""
    total_value = 0
    for number in numbers:
        total_value += number
    return total_value

def average(numbers: list) -> float:
    """Calculate the average of the given numbers in the list"""
    num_total = total(numbers)
    avg = float(num_total / len(numbers))
    return round(avg, 2)

def maximum(numbers: list) -> int:
    """Return the maximum value of the given numbers in the list"""
    max_val = numbers[0]
    for number in numbers:
        if number > max_val:
            max_val = number
    return max_val

def minimum(numbers: list) -> int:
    """Return the minimum value of the given numbers in the list"""
    min_val = numbers[0]
    for number in numbers:
        if number < min_val:
            min_val = number
    return min_val