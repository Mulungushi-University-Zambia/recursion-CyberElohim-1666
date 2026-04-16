# 1. Accept user input
original_input = input("Enter a word or phrase: ")

# 2. "Clean" the input 
# We convert to lowercase and remove spaces so 'Race Car' counts as a palindrome.
processed_word = original_input.lower().replace(" ", "")

# 3. Reverse the character array (string)
# [::-1] is a Pythonic way to say "start at the end and step backward to the beginning"
reversed_word = processed_word[::-1]

# 4. Compare the original with the reversed version
print(f"\nOriginal: {processed_word}")
print(f"Reversed: {reversed_word}")

if processed_word == reversed_word:
    print(f"Result: Yes, '{original_input}' is a palindrome!")
else:
    print(f"Result: No, '{original_input}' is not a palindrome.")
