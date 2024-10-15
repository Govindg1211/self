def get_user_input():
    user_input = input("Enter numbers separated by spaces: ")
    return [float(num) for num in user_input.split()]

def sort_array(array):
    return sorted(array)

def display_sorted_array(sorted_array):
    print("Sorted array in ascending order:", sorted_array)

def main():
    number_list = get_user_input()
    sorted_list = sort_array(number_list)
    display_sorted_array(sorted_list)

if __name__ == "__main__":
    main()