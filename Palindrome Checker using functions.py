#EMMANUEL BARAKA
#REG NO : BSCIT-05-0113/2024

# PALINDROME CHECKER
def is_palindrome(text):
    # Convert to lowercase and remove spaces for a more robust check
    cleaned_text = text.replace(" ", "").lower()
    # Check if the text is equal to its reverse
    return cleaned_text == cleaned_text[::-1]

# --- Main Program ---
user_input = input("Enter a word or phrase to check: ")

if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")
