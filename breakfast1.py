def ask_breakfast_choice():
    print("Good morning! Let's talk about breakfast.")
    print("What would you like to have for breakfast?")
    
    # List of breakfast options
    breakfast_options = [
        "1. Pancakes",
        "2. Omelette",
        "3. Smoothie",
        "4. Cereal",
        "5. Toast with jam"
    ]
    
    # Display the options
    for option in breakfast_options:
        print(option)
    
    # Get user input
    choice = input("Please enter the number of your choice (1-5): ")
    
    # Respond based on the user's choice
    if choice == '1':
        print("Pancakes! Great choice! Fluffy and delicious!")
    elif choice == '2':
        print("Omelette! A classic protein-packed option!")
    elif choice == '3':
        print("Smoothie! Healthy and refreshing, perfect for a busy morning!")
    elif choice == '4':
        print("Cereal! Quick and easy, just like your mornings!")
    elif choice == '5':
        print("Toast with jam! Simple yet satisfying!")
    else:
        print("Hmm, that doesn't seem like a valid option. Maybe just grab a coffee instead!")

if __name__ == "__main__":
    ask_breakfast_choice()