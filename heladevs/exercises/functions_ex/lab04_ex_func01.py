# Looping Techniques
# Print odd numbers from 1 to 30
def is_odd(num: int) -> bool:
    """ Function for checking whether the number is odd or even"""
    if num % 2 == 0:
        return True
    else:
        return False

for number in range(1, 31):
    if is_odd(number):
        print(number, end = " " )
