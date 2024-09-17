# Importing necessary libraries
import pandas as pd  # Pandas is used for data manipulation and analysis
import numpy as np   # NumPy is used for numerical operations on arrays
import math          # Math provides access to mathematical functions

# Function using pandas
def create_dataframe(data):
    """
    Creates a DataFrame from a given dictionary.
    
    Parameters:
    data (dict): A dictionary where keys are column names and values are lists of column data.

    Returns:
    DataFrame: A pandas DataFrame constructed from the input data.
    """
    df = pd.DataFrame(data)
    return df

# Function using numpy
def calculate_mean(numbers):
    """
    Calculates the mean of a list of numbers using NumPy.
    
    Parameters:
    numbers (list): A list of numerical values.

    Returns:
    float: The mean of the input numbers.
    """
    return np.mean(numbers)

# Function using math
def calculate_square_root(value):
    """
    Calculates the square root of a given number using the math library.
    
    Parameters:
    value (float): A non-negative number to find the square root of.

    Returns:
    float: The square root of the input value.
    
    Raises:
    ValueError: If the input value is negative.
    """
    if value < 0:
        raise ValueError("Cannot compute square root of a negative number.")
    
    return math.sqrt(value)

# Example usage
if __name__ == "__main__":
    # Example data for pandas
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    
    # Creating a DataFrame
    df = create_dataframe(data)
    print("DataFrame:")
    print(df)
    
    # Example list for numpy
    numbers = [10, 20, 30, 40, 50]
    
    # Calculating mean
    mean_value = calculate_mean(numbers)
    print("\nMean of numbers:", mean_value)
    
    # Example value for math
    value = 16
    
    # Calculating square root
    sqrt_value = calculate_square_root(value)
    print("\nSquare root of", value, "is:", sqrt_value)