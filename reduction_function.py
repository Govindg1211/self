from functools import reduce
import operator

numbers = [1, 2, 3, 4, 5]
sum_result = reduce(lambda x, y: x + y, numbers)
print(f"Sum of the list: {sum_result}") 
def multiply(x, y):
    return x * y

product_result = reduce(multiply, numbers)
print(f"Product of the list: {product_result}")
sum_with_operator = reduce(operator.add, numbers)
print(f"Sum using operator.add: {sum_with_operator}") 

product_with_operator = reduce(operator.mul, numbers)
print(f"Product using operator.mul: {product_with_operator}")
max_value = reduce(lambda a, b: a if a > b else b, numbers)
print(f"Maximum value in the list: {max_value}")  
strings = ["Hello", " ", "World", "!"]
concatenated_string = reduce(lambda x, y: x + y, strings)
print(f"Concatenated string: {concatenated_string}")  