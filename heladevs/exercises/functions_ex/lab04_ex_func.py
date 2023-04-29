# Looping Techniques
# Print odd numbers from 1 to 30
def print_odd_numbers(start: int, stop: int) -> list:
    odd_numbers = []
    for num in range(start, stop):
        if num % 2 != 0:
            odd_numbers.append(num)
            num += 1
    return odd_numbers

print("Odd numbers from 1 to 30 : ", print_odd_numbers(1, 30))

# Calculate the total, average, maximum and minimum using a looping technique
def total(numbers: list) -> int:
    answer = 0
    for num in numbers:
        answer += num
    return answer

def average(numbers: list) -> float:
    num_total = total(numbers)
    return float(num_total / len(numbers))

def maximum(numbers: list) -> int:
    max_val = 0
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val

def minimum(numbers: list) -> int:
    min_val = numbers[0]
    for num in numbers:
        if num < min_val:
            min_val = num
    return min_val

numbers = [45, 93, 34, 71, 89, 56]
print("Total : ", total(numbers))
print("Average : ", average(numbers))
print("Maximum : ", maximum(numbers))
print("Minimum : ", minimum(numbers))

# Multiplication Table upto 10 for given number
def multiply(num: int) -> None:
    for i in range(0, 10):
        print(f"{num} x {i + 1} = {num * (i + 1)}")

num = input("Enter an integer : ")
if not num.isdigit():
    print("Please! enter positive integer")
    exit(0)
multiply(int(num))

# Get 10 names from user inputs, count the names starting with B and display
def find_names():
    names = []
    for i in range(10):
        name = input(f"Enter Name {i + 1} : ")
        if name[0].capitalize() == "B":
            names.append(name.capitalize())
    return names, len(names)

names, count = find_names()
print("Names starting With letter \"B\" : ", names)
print("Count of the names : ", count)
