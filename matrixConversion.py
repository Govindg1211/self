def create_matrix():
    # Get the dimensions of the matrix from the user
    dimensions = input("Enter the dimensions of the matrix (e.g., 2x2, 3x3): ")
    
    try:
        # Split the dimensions and convert them to integers
        rows, cols = map(int, dimensions.lower().split('x'))
        
        # Initialize an empty matrix
        matrix = []
        
        print(f"Enter the elements for a {rows}x{cols} matrix:")
        
        # Loop to input each row
        for i in range(rows):
            while True:
                try:
                    # Input elements for each row
                    row_input = input(f"Row {i + 1} (space-separated values): ")
                    row = list(map(int, row_input.split()))
                    
                    # Check if the row has the correct number of columns
                    if len(row) != cols:
                        print(f"Please enter exactly {cols} numbers.")
                        continue
                    
                    matrix.append(row)
                    break  # Exit loop if row is valid
                
                except ValueError:
                    print("Invalid input. Please enter integers only.")
        
        # Print the resulting matrix
        print("\nThe resulting matrix is:")
        for row in matrix:
            print(row)
    
    except ValueError:
        print("Invalid dimensions. Please enter in the format 'NxM' (e.g., 2x2).")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
create_matrix()