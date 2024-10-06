# Function to create an array from user input
def create_array():
    while True:
        try:
            # Ask the user how many values they want to enter
            num_values = int(input("Enter the number of values you want to input: "))
            if num_values <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # Initialize an empty list to store the values
    values = []

    # Loop to get the specified number of inputs
    for i in range(num_values):
        while True:
            try:
                value = int(input(f"Enter value {i + 1}: "))  # Get each value as an integer
                values.append(value)  # Append the value to the list
                break  # Exit the inner loop if input is valid
            except ValueError:
                print("Invalid input. Please enter a valid integer.")

    return values

# Main execution
if __name__ == "__main__":
    result_array = create_array()
    print("The array you created is:", result_array)