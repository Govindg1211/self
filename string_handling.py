
greeting = "Hello, World!"
name = "Alice"

full_greeting = greeting + " My name is " + name
print(full_greeting)  

length = len(full_greeting)
print(f"Length of the full greeting: {length}") 
first_five_chars = full_greeting[:5]
print(f"First five characters: {first_five_chars}")  

upper_case = full_greeting.upper()
lower_case = full_greeting.lower()
print(f"Uppercase: {upper_case}")  
print(f"Lowercase: {lower_case}")  

index_of_name = full_greeting.find("Alice")
if index_of_name != -1:
    print(f"'Alice' found at index: {index_of_name}")  
else:
    print("'Alice' not found.")

new_greeting = full_greeting.replace("Alice", "Bob")
print(new_greeting)  

words = full_greeting.split()
print("Words in the greeting:", words)  
joined_string = " ".join(words)
print("Joined string:", joined_string)  
age = 30
formatted_string = f"{name} is {age} years old."
print(formatted_string) 