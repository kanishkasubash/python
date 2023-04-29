# Get 10 names from user inputs,
# count the names start with B and display those names at the end
name_list = []
for i in range(10):
    name = input("Enter Name : ")
    if name[0].capitalize() == "B":
        name_list.append(name.capitalize())

name_count = len(name_list)
if name_count == 0:
    print("No names start with letter 'B' ")
else:
    print("Name Count : ", name_count)
    print("Name(s) start with letter 'B' : ", name_list)
