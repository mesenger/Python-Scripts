#Create a liters_to_m3 function that:

#1. gets a liters parameter

#2. converts liters to cubic meters knowing that 1000 liters are equal to 1 cubic meter and returns the cubic meters.

def liters_to_m3(liters):
    cubic_meters = liters / 1000
    return cubic_meters

# The function should:

# 1. get a password argument

# 2. return the string "Strong Password" if all of the following conditions are true:

# Eight or more characters

# At least one uppercase letter.

# At least one digit.

# 3. returns "Weak Password" if at least one of the three conditions is not met.

# def strength(password):
#     if len(password) >= 8 and any(char.isupper() for char in password) and any(char.isdigit() for char in password):
#         return "Strong Password"
#     else:
#         return "Weak Password"
    
# Define a function that takes a list as an argument and returns the average value of the list items. For example, if I called your function with foo(10, 20, 30, 40) it should return 25, the average of the numbers of the list.

# def average(*args):
#     if len(args) == 0:
#         return None  # Return None for an empty sequence
#     return sum(args) / len(args)

# def foo(mylist):
#     # Calculate the sum of all elements in the list and divide it by the length of the list
#     return sum(mylist) / len(mylist)

# foo(10,20,30,40)

# Implement a function that gets a person's name as a parameter and greets the person with Hi Person. For example, if I call your function using foo("lisa") the function should return Hi lisa .

# def greet(name):
#     name = name.capitalize()
#     return f"Hi {name}"

# # Implements a function that takes two strings as parameters, concatenates them and returns the result.

# def concatenate(string1, string2):
#     return string1 + string2

# print(concatenate("Hello", "World"))

def speed(distance_time):
    distance = distance_time[0]
    time = distance_time[1]
    return distance / time
        
print(speed([200, 4]))