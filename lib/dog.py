#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

# class Dog:
#     def __init__(self) :
#         self._name = None
#     def name(self):
#         return self._name
#     def name(self, value):
#         if isinstance(value, str) and 1 <= len(value) <= 25:
#             self._name = value
#          else:
#            print("Name must be a string between 1 and 25 characters.")
    
# my_dog = Dog()
# my_dog.name = "relax"
# print(my_dog.name)
# my_dog.name="ThisIsAVeryLongNameForADog111111111111" 
# print(my_dog.name)

class Dog:
    def __init__(self):
        self._name = None  # Private attribute to store the name
        self._breed = None


    def breed (self):
        return self._breed
    
    def breed (self ,value):
         if value in self.approved_breeds:
            self._breed = value
         else : 
            print( " The breed must be in the following list of dog breeds")
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value
        else:
            print("Name must be a string between 1 and 25 characters.")
            return  # Exit the setter without setting the name
    
# Creating a Dog object
my_dog = Dog()

# Setting the name using the property
my_dog.name = "Buddy"  # Valid name
my_dog.breed = "xxxx"
print(my_dog.breed)
# Accessing the name using the property
print(my_dog.name)  # Output: Buddy

# Trying to set an invalid name
my_dog.name = "ThisIsAVeryLongNameForADog"  # Invalid name
# Output: Name must be a string between 1 and 25 characters.

# Checking the name again to confirm it wasn't changed due to an invalid input
print(my_dog.name)  # Output: Buddy
