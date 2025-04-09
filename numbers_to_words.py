def validate_number(number):
    if number < 1000 or number > 9999:
        return "Please enter a 4-digit number."
    return None

def number_to_string_recursive_real(number):
    """
    Recursively converts a 4-digit number to its string representation.

    Args:
        number (int): A 4-digit integer.

    Returns:
        str: The string representation of the number.
    """
    ones = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    place_names = ["thousand", "hundred", "ten", ""]

    def recursive_helper(n, index):
        # Base case: Stop recursion when all 4 digits have been processed
        if index >= 4:
            return ""

        digit = int(n[index])
        # Skip zero digits (do not include them in the word output)
        if digit == 0:
            return recursive_helper(n, index + 1)

        # Handle 'teen' numbers like 11, 12, ..., 19
        if index == 2 and digit == 1:
            teen_number = int(n[2:4])
            teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", 
                     "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
            return teens[int(n[3])] + " "

        # Convert digit to its word representation
        word = ones[digit]
        if place_names[index]:
            word += f" {place_names[index]}"
        return word + " " + recursive_helper(n, index + 1 if not (index == 2 and digit == 1) else 4)

    return recursive_helper(str(number), 0).strip()

# Prompt the user to enter a 4-digit number and handle invalid inputs
while True:
    user_input = input("Please enter a 4-digit number: ")
    if user_input.lower() in ['q', 'quit']:
        print("Goodbye!")
        break
    try:
        number = int(user_input)
        if number < 1000 or number > 9999:
            print("Please enter a 4-digit number.")
        else:
            result = number_to_string_recursive_real(number)
            print(f"The written form of the number '{number}' is: {result}")
            break  # Exit after successful input
    except ValueError:
        print("Invalid input. Please enter a numeric 4-digit number.")
