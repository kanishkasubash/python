def add(num1: int, num2: int) -> int:
    return num1 + num2

def sub(num1: int, num2: int) -> int:
    return num1 - num2

def mul(num1: int, num2: int) -> int:
    return num1 * num2

def div(num1: int, num2: int) -> float:
    if num2 == 0:
        return 0
    else:
        return num1 / num2