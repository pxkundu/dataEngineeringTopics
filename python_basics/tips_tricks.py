import os
import logging
import pandas as pd
from dotenv import load_dotenv

# Logging Configuration
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

# Section 1: Mutable Data Types
logging.info("--- Section 1: Mutable Data Types ---")
list_a = [1, 2, 3]
list_b = list_a.copy()  # Use copy to avoid modifying original
list_b.append(4)
print("list_a:", list_a)
print("list_b:", list_b)

# Section 2: File Handling
logging.info("--- Section 2: File Handling ---")
# Writing and reading files efficiently
with open("example.txt", "w") as file:
    file.write("Data Engineering Example File\n")

with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())

# Section 3: Avoid Hardcoding Paths
logging.info("--- Section 3: Avoid Hardcoding Paths ---")
base_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(base_dir, "data", "example.csv")
print("File Path:", file_path)

# Section 4: Handle Missing Data
logging.info("--- Section 4: Handle Missing Data ---")
data = {"Name": ["Alice", "Bob", None], "Age": [30, None, 25]}
df = pd.DataFrame(data)
df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)
print(df)

# Section 5: Efficient Chunk Processing
logging.info("--- Section 5: Efficient Chunk Processing ---")
# Simulate chunk processing
chunk_size = 2  # Example chunk size
example_data = [1, 2, 3, 4, 5, 6]
for i in range(0, len(example_data), chunk_size):
    chunk = example_data[i:i + chunk_size]
    print("Processing chunk:", chunk)

# Section 6: SQL-Like Querying with Pandas
logging.info("--- Section 6: SQL-Like Querying with Pandas ---")
data = {"Name": ["Alice", "Bob", "Charlie"], "Salary": [70000, 50000, 60000]}
df = pd.DataFrame(data)
high_salary = df.query("Salary > 55000")
print(high_salary)

# Section 7: List Comprehensions
logging.info("--- Section 7: List Comprehensions ---")
squares = [x**2 for x in range(10)]
print("Squares:", squares)

# Section 8: Enumerate
logging.info("--- Section 8: Enumerate ---")
items = ["apple", "banana", "cherry"]
for index, item in enumerate(items):
    print(f"{index}: {item}")

# Section 9: Using Config Files for Parameters
logging.info("--- Section 9: Using Config Files ---")
load_dotenv()  # Load .env file
db_url = os.getenv("DATABASE_URL", "default_value")
print("Database URL:", db_url)

# Section 10: Logging and Exception Handling
logging.info("--- Section 10: Logging and Exception Handling ---")
def divide_numbers(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        logging.error("Division by zero is not allowed!")
        return None
    except TypeError:
        logging.error("Invalid data type provided!")
        return None

print("Division Result:", divide_numbers(10, 0))
print("Division Result:", divide_numbers(10, "a"))

logging.info("--- End of Script ---")
