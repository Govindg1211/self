def breakfast_menu():
    # Welcome the user
    user_name = input("Welcome! What's your name? ")
    print(f"\nHello, {user_name}! What would you like to have for breakfast?")
    
    # Define breakfast options
    menu_options = {
        1: "Pancakes",
        2: "Omelette",
        3: "Fruit Salad",
        4: "Cereal",
        5: "Smoothie"
    }
    
    # Display the menu
    print("\nBreakfast Menu:")
    for key, value in menu_options.items():
        print(f"{key}. {value}")
    
    # Get user choice
    try:
        choice = int(input("\nPlease enter the number of your choice: "))
        
        # Validate choice
        if choice in menu_options:
            print(f"\nGreat choice, {user_name}! Enjoy your {menu_options[choice]}!")
        else:
            print("\nInvalid choice. Please select a number from the menu.")
    except ValueError:
        print("\nInvalid input. Please enter a number.")

# Run the breakfast menu function
breakfast_menu()