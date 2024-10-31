# Function to calculate the ASCII value sum of a name
def ascii_sum(name):
    total = 0
    for char in name:
        total += ord(char)  # ord() function returns the ASCII value of the character
    return total

# Main program
def main():
    # Ask the user for their name
    user_name = input("What is your name? ")
    
    # Calculate the ASCII sum
    total_ascii_value = ascii_sum(user_name)
    
    # Print the result
    print(f"The sum of the ASCII values of your name '{user_name}' is: {total_ascii_value}")

# Run the main program
if __name__ == "__main__":
    main()