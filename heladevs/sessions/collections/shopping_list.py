shopping_list = ["Apple", "Banana"]

# Add items in the end of the list 
shopping_list.append("Milk")
shopping_list.append("Salt")
shopping_list.append("Egg")

# Print All items in the shopping list
for item in shopping_list:
    print(item)

# Remove items at the end of the list
shopping_list.pop()

# Remove specific item of the list
shopping_list.remove("Banana")

# Inssert item into specific index
shopping_list.insert(1, "Avacado")

print(shopping_list)