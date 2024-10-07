def get_greeting_style():
    """Function to get the user's preferred greeting style."""
    print("Choose a greeting style:")
    print("1. Hello")
    print("2. Hi")
    print("3. Greetings")
    print("4. Salutations")

    choice = input("Enter the number of your choice (1-4): ")
    
    if choice == '1':
        return "Hello"
    elif choice == '2':
        return "Hi"
    elif choice == '3':
        return "Greetings"
    elif choice == '4':
        return "Salutations"
    else:
        print("Invalid choice, defaulting to 'Hello'.")
        return "Hello"

def main():
    """Main function to run the greeting program."""
    while True:
        # Get user's preferred greeting style
        greeting_style = get_greeting_style()
        
        # Get user input
        user_input = input("Please enter a word: ").strip()
        
        # Input validation
        if not user_input:
            print("You didn't enter a word! Please try again.")
            continue
        
        # Create a greeting message
        greeting_message = f"{greeting_style}! You entered: {user_input}"
        
        # Print the greeting message
        print(greeting_message)
        
        # Ask if the user wants to continue
        continue_choice = input("Would you like to enter another word? (yes/no): ").strip().lower()
        
        if continue_choice != 'yes':
            print("Thank you for using the greeting program! Goodbye!")
            break

# Run the program
if __name__ == "__main__":
    main()