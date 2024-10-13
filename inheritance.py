# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

# Derived class
class Dog(Animal):
    def speak(self):
        return f"{self.name} barks."

# Creating instances of the classes
animal = Animal("Generic Animal")
dog = Dog("Buddy")

# Calling methods
print(animal.speak())  # Output: Generic Animal makes a sound.
print(dog.speak())     # Output: Buddy barks.