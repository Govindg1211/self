import random

def guessing_game():
    # Welcome the user
    user_name = input("Welcome! What's your name? ")
    print(f"\nHello, {user_name}! Let's play a guessing game.")
    
    # Set the game difficulty
    difficulty = input("\nChoose a difficulty level (easy, medium, hard): ").lower()
    
    # Set the range based on difficulty
    if difficulty == "easy":
        start = 1
        end = 10
    elif difficulty == "medium":
        start = 1
        end = 20
    elif difficulty == "hard":
        start = 1
        end = 50
    else:
        print("\nInvalid difficulty level. Setting to easy.")
        start = 1
        end = 10
    
    # Generate a random number
    secret_number = random.randint(start, end)
    
    # Set the number of attempts based on difficulty
    if difficulty == "easy":
        attempts = 5
    elif difficulty == "medium":
        attempts = 3
    else:
        attempts = 2
    
    # Play the game
    while attempts > 0:
        try:
            guess = int(input(f"\nGuess a number between {start} and {end}: "))
            
            if guess == secret_number:
                print(f"\nCongratulations, {user_name}! You guessed the number correctly.")
                break
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
            
            attempts -= 1
            print(f"Attempts left: {attempts}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    if attempts == 0:
        print(f"\nSorry, {user_name}. You ran out of attempts. The number was {secret_number}.")

# Run the guessing game
guessing_game()