# Halloween Snack Selector

def halloween_snack():
    print("🎃 Welcome to the Halloween Snack Selector! 🎃")
    print("What would you like to have for a Halloween snack?")
    
    # List of possible snacks
    snacks = [
        "Candy Corn",
        "Pumpkin Pie",
        "Caramel Apples",
        "Chocolate Bars",
        "Ghost-shaped Cookies",
        "Popcorn Balls"
    ]
    
    # Display the snack options
    for index, snack in enumerate(snacks, start=1):
        print(f"{index}. {snack}")
    
    # Ask the user for their choice
    try:
        choice = int(input("Please enter the number of your favorite snack (1-6): "))
        
        if 1 <= choice <= len(snacks):
            selected_snack = snacks[choice - 1]
            print(f"You've chosen {selected_snack}! Enjoy your Halloween! 🎉")
        else:
            print("Invalid choice. Please select a number between 1 and 6.")
    except ValueError:
        print("That's not a valid number! Please enter a number between 1 and 6.")

# Run the function
halloween_snack()