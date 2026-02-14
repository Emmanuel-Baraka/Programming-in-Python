#EMMANUEL BARAKA
#REG NO : BSCIT-05-0113/2024

# EVEN NUMBERS
def get_even_numbers(numbers):
    # Creates a new list containing only even integers
    new_list = [n for n in numbers if n % 2 == 0]
    return new_list

# --- Main Program ---

# 1. Ask the user for input
# We use input() to get a string of numbers separated by spaces
user_input = input("Enter a list of numbers separated by spaces: ")

# 2. Convert the input string into a list of integers
# .split() breaks the string into a list of strings: ["1", "2", "3"]
# int(x) converts each string into an integer
try:
    original_list = [int(x) for x in user_input.split()]

    # 3. Call the function and store the result in a new variable
    even_list = get_even_numbers(original_list)

    # 4. Print the results
    print("\nYour List:", original_list)
    print("New List (Evens Only):", even_list)

except ValueError:
    print("Error: Please ensure you only enter whole numbers separated by spaces.")
