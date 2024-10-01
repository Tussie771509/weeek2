# Accepting user input to create two sets of integers
set1_input = input("Enter the first set of integers separated by spaces: ")
set1 = {int(num) for num in set1_input.split()}

set2_input = input("Enter the second set of integers separated by spaces: ")
set2 = {int(num) for num in set2_input.split()}

# Creating a new set that contains only the elements common to both sets
common_elements = set1.intersection(set2)

print("Common elements:", common_elements)
