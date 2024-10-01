# Accepting user input to create a list of integers
user_input = input("Enter integers separated by spaces: ")
integer_list = [int(num) for num in user_input.split()]

# Computing the sum of all integers in the list
total_sum = sum(integer_list)
print(f"The sum of the integers is: {total_sum}")
