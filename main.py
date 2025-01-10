def add_numbers(num1, num2): # defined a function add_numbers
     return num1 + num2
     
result = add_numbers(5, 6) # calling the function with 2 numbers
print("The sum is :", result) 


def is_even(number): #function with one parameter
     if number % 2 == 0: # used % so that it can be divided and it should not have a remainder
          return True
     else :
          return False

result = is_even(9) #testing to see result if is true or false
print (result)  


def reverse_string(text):
     return text[::-1] #slicing technique
     #takes the string and puts it in reverse in order 

reversed_text = reverse_string("maekins") #testing to check if it is reversed
print(reversed_text)


def count_vowels(text):
     vowels = "aeioAEIOUu"#vowels in lower and uppercase
     count = 0

     #loop trough each character
     for char in text:
          if char in vowels:
               count += 1

     return count   
     #test the function
vowel_count = count_vowels("jamaica")
print(vowel_count)       


def calculate_factorial(n):
     #initializing the result to 1 factorial 
     result = 1
     #multipling the result by each integer from 1 to n
     for i in range (1, n + 1):
          result *= i

     return result

factorial_result = calculate_factorial(3)
print(factorial_result)     


# Define the decorator function
def decorator_func(func):
    def wrapper(*args, **kwargs):
        print("Decorator Applied")  # Print message before calling the original function
        return func(*args, **kwargs)  # Call the original function
    return wrapper

# Define the apply_decorator function
def apply_decorator(func):
    # Apply the decorator to the function and return the decorated version
    return decorator_func(func)

# Example function to test the decorator
def mapangale():
    print("Gothe rera!")

# Apply the decorator using apply_decorator
decorated_function = apply_decorator(mapangale)

# Call the decorated function
decorated_function()  # This will print "Decorator Applied" and then "Hello, World!"


# Function to sort list of tuples by age
def sort_by_age(persons):
    return sorted(persons, key=lambda x: x[1])

# Example usage
persons_list = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
sorted_persons = sort_by_age(persons_list)
print(sorted_persons)  # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]



# Function to merge dictionaries and sum common keys
def merge_dicts(dict1, dict2):
    merged = dict1.copy()  # Start with a copy of the first dictionary
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Sum the values for common keys
        else:
            merged[key] = value  # Add the key-value pair if not present
    return merged


dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
merged_dict = merge_dicts(dict1, dict2)
print(merged_dict)  # Output: {'a': 1, 'b': 5, 'c': 4}



# Class definition for Car
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")


my_car = Car("Toyota", "Corolla", 2020)
my_car.display_info()  # Output: Car Info: 2020 Toyota Corolla

