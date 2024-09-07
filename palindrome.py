# Palindrome Checker in Python

def is_palindrome(word):
    # Normalize the word by removing spaces and converting to lowercase
    normalized_word = ''.join(word.split()).lower()
    # Check if the normalized word is the same as its reverse
    return normalized_word == normalized_word[::-1]

def main():
    print("Welcome to the Palindrome Checker!")
    
    while True:
        # Take input from the user
        user_input = input("Enter a word or phrase to check if it's a palindrome: ")
        
        if is_palindrome(user_input):
            print(f'"{user_input}" is a palindrome!')
        else:
            print(f'"{user_input}" is not a palindrome.')
        
        # Ask if the user wants to check another word
        another_check = input("Do you want to check another word? (yes/no): ")
        if another_check.lower() != 'yes':
            print("Thank you for using the Palindrome Checker! Goodbye!")
            break

if __name__ == "__main__":
    main()