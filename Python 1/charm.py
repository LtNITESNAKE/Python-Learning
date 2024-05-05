# Variables and Data Types:
x = 5
name = "Alice"
is_valid = True

# Basic Operators:
result = 10 + 5
difference = 20 - 8
product = 4 * 6
quotient = 15 / 3
remainder = 17 % 4

# Conditional Statements:
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Loops:
# For Loop:
for i in range(5):
    print(i)
    
# While Loop:
num = 0
while num < 5:
    print(num)
    num += 1

# Functions:
def add(x, y):
    return x + y

result = add(3, 4)
print(result)

# Lists, Tuples, Dictionaries, Sets:
# Lists:
my_list = [1, 2, 3, 4, 5]

# Tuples:
my_tuple = (1, 2, 3)

# Dictionaries:
my_dict = {'name': 'Alice', 'age': 30}

# Sets:
my_set = {1, 2, 3, 4, 5}

# List Comprehensions:
numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]

# Exception Handling:
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Modules and Packages:
import math

# Classes and Objects:
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

my_circle = Circle(5)
print(my_circle.area())

# File Handling:
with open('example.txt', 'w') as file:
    file.write("Hello, World!")
