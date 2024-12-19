# Python Basics Consolidated Learning Code

import os
import logging
import pandas as pd
from dotenv import load_dotenv

# Logging Configuration
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Section 1: Variables and Data Types
logging.info("--- Section 1: Variables and Data Types ---")
# Practice Task 1: Define variables of different data types and print them
name = "John Doe"
age = 25
height = 5.9  # in feet
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Section 2: Lists and Loops
logging.info("--- Section 2: Lists and Loops ---")
# Practice Task 2: Create a list of numbers and find their sum using a loop
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total += number
print("Sum of Numbers:", total)

# Section 3: Dictionaries
logging.info("--- Section 3: Dictionaries ---")
# Practice Task 3: Define a dictionary and loop through its keys and values
personal_details = {
    "Name": "John Doe",
    "Age": 25,
    "Role": "Data Engineering Learner"
}

print("Personal Details:")
for key, value in personal_details.items():
    print(f"{key}: {value}")

# Section 4: Functions
logging.info("--- Section 4: Functions ---")
# Practice Task 4: Write a function to calculate the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

numbers = [10, 20, 30, 40, 50]
print("Average of Numbers:", calculate_average(numbers))

# Section 5: Exception Handling
logging.info("--- Section 5: Exception Handling ---")
# Practice Task 5: Write a function to divide two numbers with exception handling
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Division by zero is not allowed!")
        return None
    except TypeError:
        logging.error("Invalid data type provided!")
        return None

print("Division Result:", divide_numbers(10, 2))
print("Division Result:", divide_numbers(10, 0))
print("Division Result:", divide_numbers(10, "a"))

# Section 6: File Handling
logging.info("--- Section 6: File Handling ---")
# Practice Task 6: Write data to a file and read it back
with open("data.txt", "w") as file:
    file.write("Name,Age,Role\n")
    file.write("Alice,30,Engineer\n")
    file.write("Bob,25,Data Analyst\n")

with open("data.txt", "r") as file:
    content = file.readlines()
    for line in content:
        print(line.strip())

# Section 7: Mutable Data Types
logging.info("--- Section 7: Mutable Data Types ---")
# Practice Task 7: Demonstrate mutability in lists and how to avoid it
list_a = [1, 2, 3]
list_b = list_a.copy()  # Use copy to avoid modifying original
list_b.append(4)
print("list_a:", list_a)
print("list_b:", list_b)

# Section 8: Efficient Chunk Processing
logging.info("--- Section 8: Efficient Chunk Processing ---")
# Simulate chunk processing
chunk_size = 2  # Example chunk size
example_data = [1, 2, 3, 4, 5, 6]
for i in range(0, len(example_data), chunk_size):
    chunk = example_data[i:i + chunk_size]
    print("Processing chunk:", chunk)

# Section 9: SQL-Like Querying with Pandas
logging.info("--- Section 9: SQL-Like Querying with Pandas ---")
data = {"Name": ["Alice", "Bob", "Charlie"], "Salary": [70000, 50000, 60000]}
df = pd.DataFrame(data)
high_salary = df.query("Salary > 55000")
print(high_salary)

# Section 10: List Comprehensions
logging.info("--- Section 10: List Comprehensions ---")
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Section 11: Enumerate
logging.info("--- Section 11: Enumerate ---")
items = ["apple", "banana", "cherry"]
for index, item in enumerate(items):
    print(f"{index}: {item}")

# Section 12: Using Config Files for Parameters
logging.info("--- Section 12: Using Config Files ---")
load_dotenv()  # Load .env file
db_url = os.getenv("DATABASE_URL", "default_value")
print("Database URL:", db_url)

logging.info("--- End of Script ---")
