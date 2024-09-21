def print_multiplication_table(number, start=1, end=10):
    """Prints the multiplication table for the given number from start to end."""
    print(f"\nMultiplication Table for {number} (from {start} to {end}):\n" + "-"*40)
    for i in range(start, end + 1):
        print(f"{number} x {i:2} = {number * i:4}")
    print("-"*40)

def main():
    try:
        # Get the number from the user
        number = int(input("Enter a number for which you want the multiplication table: "))

        # Get the starting and ending range for the table
        start = int(input("Enter the starting range (default is 1): ") or 1)
        end = int(input("Enter the ending range (default is 10): ") or 10)

        # Validate the range inputs
        if start > end:
            print("Error: Starting range cannot be greater than ending range.")
            return

        # Print the multiplication table
        print_multiplication_table(number, start, end)
    except ValueError:
        print("Error: Please enter valid integers only.")

# Run the main function
if __name__ == "__main__":
    main()
