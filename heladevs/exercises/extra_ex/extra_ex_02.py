# 2. Odd even checker
# Write a program to get a user input and check whether
# it's a odd or even number
input_val = input("Enter the number : ")
number = int(input_val)
num_mod = number % 2
if num_mod == 0:
    print("This is an even number!")
else:
    print("This is an odd number!")