# School grade calculator
# Write a program to get 5 inputs for different school subjects
# and calculate Average score
count = 0
total = 0
average_score = 0
for i in range(5):
    input_val = input("Enter Marks: ")
    total += float(input_val)
    count += 1
average_score = total / count
print("Average Score : ", average_score)