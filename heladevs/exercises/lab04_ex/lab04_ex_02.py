# Calculate the total, average and maximum, minimum values in the list
numbers = [45, 93, 34, 71, 89, 56]
count = 0
total = 0

for value in numbers:
    total += value
    count += 1

average = total / count
minimum = min(numbers)
maximum = max(numbers)

print("Total : ", total)
print("Average : ", average)
print("Minimum : ", minimum)
print("Maximum : ", maximum)
