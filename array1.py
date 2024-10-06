# Function to create an array from user input
def create_array():
    user_input = input("Enter values separated by spaces: ")
    
    array = user_input.split()
    
    
    return array

# Main execution
if __name__ == "__main__":
    result_array = create_array()
    print("You entered the following array:")
    print(result_array)