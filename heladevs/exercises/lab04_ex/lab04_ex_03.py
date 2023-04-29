# Prompt user to provide a positive integer,
# Then print the multiplication table upto 10
input_value = input("Enter an integer: ")
number = int(input_value)
if number < 0:
    print("Please! provide a positive integer")
else:
    count = 1
    while count <= 10:
        print(number, " X ", count, " = ", number*count)
        count += 1
