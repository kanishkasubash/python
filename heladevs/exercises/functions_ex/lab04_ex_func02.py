# Calculate the total, average, maximum and minimum using a looping technique
import numberutil as numutil

numbers = [45, 93, 34, 71, 89, 56]

total = numutil.total(numbers)
average = numutil.average(numbers)
minimum = numutil.maximum(numbers)
maximum = numutil.minimum(numbers)

print(f"Total : {total}")
print(f"Average : {average}")
print(f"Maximum : {minimum}")
print(f"Minimum : {maximum}")