# Print odd numbers from 1 to 30 using a loop
odd_numbers = []
for number in range(1, 31):
    val = number % 2
    if val == 1:
        odd_numbers.append(number)

print("Odd Numbers from 1 to 30 : ", odd_numbers)
