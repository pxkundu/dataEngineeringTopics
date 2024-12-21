# dataEngineeringTopics
Storage for my Data Engineering learning and reference codebase

We will proceed step by step through the outline, starting from **Module 1**, treating you as a beginner and building concepts with hands-on code examples. I will pick **Python** as the language to start since it is beginner-friendly, widely used in data engineering, and covered in your outline.

Let’s begin! 🚀

---

## **Module 1: Basics**

### **1.1 Introduction to Linux**
Since the outline begins with Linux basics, we'll start here.

**Goal:**
- Learn essential Linux commands to navigate and interact with a Linux environment.

---

### **Step 1: Setting up the Linux Environment**

#### **Option 1: Using Virtual Machines**
- Install **VirtualBox** or **VMware**.
- Download a **Ubuntu LTS** ISO image (free Linux distribution).

#### **Option 2: Using Windows Subsystem for Linux (WSL)**
- For Windows users:
   1. Open PowerShell as Administrator.
   2. Run the following command:
      ```bash
      wsl --install
      ```
   3. Restart your computer and install **Ubuntu** from the Microsoft Store.

---

### **Step 2: Basic Linux Commands**

Let’s explore some essential Linux commands:

1. **Navigation Commands**  
   ```bash
   pwd           # Print the current directory
   ls            # List files in the current directory
   cd /path/to/dir  # Change directory
   cd ~          # Go to home directory
   ```

2. **File and Directory Operations**
   ```bash
   mkdir my_folder       # Create a directory
   touch my_file.txt     # Create an empty file
   cp my_file.txt copy_file.txt  # Copy a file
   mv my_file.txt new_name.txt   # Rename or move a file
   rm new_name.txt       # Delete a file
   rmdir my_folder       # Delete a directory (only if empty)
   ```

3. **File Viewing**
   ```bash
   cat my_file.txt      # View file content
   less my_file.txt     # View content page by page
   head my_file.txt     # Show first 10 lines
   tail my_file.txt     # Show last 10 lines
   ```

---

### **Practice Task 1:**
1. Create a directory named `data_engineering_basics`.
2. Inside that directory:
   - Create a file named `linux_notes.txt`.
   - Write "Learning Linux Basics" into the file.
3. Copy the file to a new file called `backup_linux_notes.txt`.
4. List the files and directories.

**Commands to Use:**
```bash
mkdir data_engineering_basics
cd data_engineering_basics
touch linux_notes.txt
echo "Learning Linux Basics" > linux_notes.txt
cp linux_notes.txt backup_linux_notes.txt
ls
```

---

### **Step 3: Practice Linux Command-Line for Data Engineering**
Here’s an example to manipulate a dataset in Linux:

**Task: Create and Process a Simple CSV File**
1. Create a CSV file using a text editor or `echo` command.
   ```bash
   echo "Name,Age,Role" > team_data.csv
   echo "Alice,30,Engineer" >> team_data.csv
   echo "Bob,25,Data Analyst" >> team_data.csv
   echo "Charlie,28,Manager" >> team_data.csv
   ```

2. Display and confirm the file content.
   ```bash
   cat team_data.csv
   ```

3. Use `awk` to filter data where the role is "Engineer".
   ```bash
   awk -F',' '$3=="Engineer" {print $1, $2, $3}' team_data.csv
   ```

---

Here are additional **Linux commands and tasks** tailored for data engineering practice, focusing on data manipulation and file handling in Linux environments.

---

### **1. Working with Files and Data**
#### **View and Search Data in Files**
1. **`grep`**: Search for specific text in a file.
   ```bash
   grep "Engineer" team_data.csv   # Find all lines with "Engineer"
   grep -i "manager" team_data.csv  # Case-insensitive search
   ```

2. **`wc`**: Count lines, words, or characters in a file.
   ```bash
   wc team_data.csv          # Count lines, words, and characters
   wc -l team_data.csv       # Count only lines
   wc -w team_data.csv       # Count only words
   ```

3. **`cut`**: Extract specific columns from a file.
   ```bash
   cut -d',' -f1 team_data.csv    # Extract only the "Name" column
   cut -d',' -f2 team_data.csv    # Extract the "Age" column
   ```

4. **`sort`**: Sort the content of a file.
   ```bash
   sort team_data.csv            # Sort alphabetically
   sort -t',' -k2 -n team_data.csv  # Sort by Age (column 2) numerically
   ```

5. **`uniq`**: Remove duplicate lines (file must be sorted first).
   ```bash
   sort team_data.csv | uniq     # Remove duplicate rows
   ```

---

### **2. File Operations for Data Pipelines**
#### **Manipulate Large Files**
1. **Split a large file into smaller chunks**:
   ```bash
   split -l 10 team_data.csv part_   # Split into chunks of 10 lines each
   ```

2. **Merge multiple files into one**:
   ```bash
   cat part_* > merged_data.csv
   ```

3. **Find the number of rows in a large dataset**:
   ```bash
   wc -l large_dataset.csv
   ```

4. **Preview the start or end of a large file**:
   ```bash
   head -n 5 large_dataset.csv  # View the first 5 lines
   tail -n 5 large_dataset.csv  # View the last 5 lines
   ```

---

### **3. Working with Compressed Files**
#### **Handle Compressed Data**
1. **Compress a file using `gzip`**:
   ```bash
   gzip team_data.csv            # Compress the file
   ls                            # Verify the .gz file is created
   ```

2. **Decompress a file**:
   ```bash
   gunzip team_data.csv.gz
   ```

3. **View compressed data without extracting**:
   ```bash
   zcat team_data.csv.gz         # View compressed file content
   ```

4. **Combine and compress multiple files**:
   ```bash
   tar -cvf archive.tar file1.csv file2.csv
   gzip archive.tar              # Compress the archive
   ```

---

### **4. File Permissions and Ownership**
#### **Set Permissions for Files**
1. **Change file permissions**:
   ```bash
   chmod 644 team_data.csv       # Owner: read/write, Others: read-only
   chmod 755 script.sh           # Owner: read/write/execute, Others: read/execute
   ```

2. **View file permissions**:
   ```bash
   ls -l                         # List files with permissions
   ```

3. **Change file ownership**:
   ```bash
   sudo chown username:groupname team_data.csv
   ```

---

### **5. Disk Usage and File Management**
#### **Monitor Disk Space**
1. **Check file/directory sizes**:
   ```bash
   du -sh team_data.csv           # Show size of a file
   du -sh data_engineering_basics # Show size of a directory
   ```

2. **Check overall disk usage**:
   ```bash
   df -h                          # Show available and used disk space
   ```

---

### **6. Advanced Commands for Data Engineers**
#### **Working with Data Streams**
1. **Redirect output to a file**:
   ```bash
   grep "Engineer" team_data.csv > engineers.txt
   ```

2. **Pipe commands to combine operations**:
   ```bash
   cat team_data.csv | grep "Engineer" | wc -l  # Count rows with "Engineer"
   ```

3. **Find large files in a directory**:
   ```bash
   find . -type f -size +10M      # Find files larger than 10MB
   ```

#### **Download Files**
1. **Download files from the internet**:
   ```bash
   wget https://example.com/sample.csv
   curl -O https://example.com/sample.csv
   ```

---

### **Practice Task 2: Real-World Linux Use Cases**
1. Download a sample dataset using `wget` or `curl`.  
   Example:
   ```bash
   wget https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv
   ```

2. Perform the following operations:
   - Count the total number of rows and columns in the dataset.
   - Extract only the first column.
   - Sort the dataset by the second column numerically.
   - Find the number of unique entries in the first column.
   - Compress the dataset and verify its size.

---

### **Sample Solutions:**
1. Count rows and columns:
   ```bash
   wc -l airtravel.csv           # Count rows
   head -n 1 airtravel.csv | awk -F',' '{print NF}'  # Count columns
   ```

2. Extract the first column:
   ```bash
   cut -d',' -f1 airtravel.csv > first_column.txt
   ```

3. Sort by the second column:
   ```bash
   sort -t',' -k2 -n airtravel.csv > sorted_data.csv
   ```

4. Find unique entries:
   ```bash
   cut -d',' -f1 airtravel.csv | sort | uniq
   ```

5. Compress the file:
   ```bash
   gzip airtravel.csv
   ```

To **download files** in macOS, you can use the **Terminal** with commands like `curl` or `wget`. macOS comes with `curl` pre-installed, while `wget` can be installed if needed. Below are the step-by-step instructions:

---

### **Option 1: Using `curl` (Built-in on macOS)**

1. **Download a File**  
   Use the `-O` option to save the file with its original name:
   ```bash
   curl -O https://example.com/sample.csv
   ```
   Replace `https://example.com/sample.csv` with the actual URL of the file.

2. **Save File with a Custom Name**  
   Use the `-o` option to specify a custom filename:
   ```bash
   curl -o myfile.csv https://example.com/sample.csv
   ```

3. **Download Multiple Files**  
   Use `curl` multiple times to download multiple files:
   ```bash
   curl -O https://example.com/file1.csv
   curl -O https://example.com/file2.csv
   ```

4. **Resume a Download**  
   If the file download was interrupted, you can resume it:
   ```bash
   curl -C - -O https://example.com/largefile.zip
   ```

---

### **Option 2: Using `wget` (Install First)**
`wget` is not pre-installed on macOS but can be installed using Homebrew.

1. **Install Homebrew** (if not already installed):  
   Open Terminal and run:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

2. **Install `wget`**:
   ```bash
   brew install wget
   ```

3. **Download a File**:
   ```bash
   wget https://example.com/sample.csv
   ```

4. **Download and Rename the File**:
   ```bash
   wget -O myfile.csv https://example.com/sample.csv
   ```

5. **Download an Entire Directory** (recursive):
   ```bash
   wget -r -np https://example.com/directory/
   ```

---

### **Option 3: Download Files Using a Web Browser**
1. Open **Safari**, **Chrome**, or any browser.
2. Enter the file URL directly in the address bar.
3. Press **Enter**.
4. The browser will automatically download the file and save it to your **Downloads** folder.

---

### **Practice Task on macOS**
1. Open **Terminal**.
2. Download a sample file using `curl`:
   ```bash
   curl -O https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv
   ```

3. Confirm the file is downloaded by listing the files in the directory:
   ```bash
   ls
   ```

4. Open the downloaded file using a text editor or command:
   ```bash
   cat airtravel.csv
   ```
---

### **Next Steps** 🚀
Practice these commands until you’re comfortable. 

### **Linux Skills Evaluation**
Once we feel comfortable with basic Linux commands, we will move to the next part of **Module 1**: **Setting Up Python Environment and Basics of Python Programming**.


Let’s move to the **next part** of Module 1: **Setting up the Python Environment and Learning Python Basics**.

---

## **1.2 Setting Up Python Environment**

Python is widely used for data engineering tasks like data cleaning, transformation, and building pipelines. Let’s start with setting up the Python environment.

---

### **Step 1: Install Python**

1. Check if Python is already installed:
   ```bash
   python3 --version
   ```

2. If not installed:
   - **macOS/Linux**: Python 3 is pre-installed. Install or upgrade via `brew`:
     ```bash
     brew install python3
     ```

   - **Windows**:
     - Download Python from [python.org](https://www.python.org/downloads/).
     - Check the option **“Add Python to PATH”** during installation.

3. Confirm installation:
   ```bash
   python3 --version
   pip3 --version
   ```

---

### **Step 2: Setting Up a Virtual Environment**

A virtual environment keeps your Python libraries isolated, which is good practice.

1. Install `venv` if not already present:
   ```bash
   pip3 install virtualenv
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv my_env
   ```

3. Activate the environment:
   - On macOS/Linux:
     ```bash
     source my_env/bin/activate
     ```
   - On Windows:
     ```bash
     .\my_env\Scripts\activate
     ```

4. Deactivate the virtual environment:
   ```bash
   deactivate
   ```

---

### **Step 3: Installing Essential Python Libraries**

Install libraries needed for data engineering:
```bash
pip install pandas numpy matplotlib
```

Check installed packages:
```bash
pip list
```

---

## **1.3 Python Basics: Key Concepts**

Let’s start with **basic Python concepts** step-by-step.

---

### **Topic 1: Variables and Data Types**

#### **Code Example**
Create a file `basics.py` and write:
```python
# Variables and Data Types
name = "Alice"
age = 30
is_engineer = True
salary = 75000.50

# Print variables
print("Name:", name)
print("Age:", age)
print("Is Engineer:", is_engineer)
print("Salary:", salary)

# Data type checking
print(type(name))
print(type(age))
print(type(is_engineer))
print(type(salary))
```

**Run the code**:
```bash
python3 basics.py
```

---

### **Topic 2: Lists and Loops**

#### **Code Example**
```python
# List and Loops
team = ["Alice", "Bob", "Charlie"]

# Loop through a list
for member in team:
    print("Team Member:", member)

# Add and remove items
team.append("David")
print("After Adding:", team)

team.remove("Bob")
print("After Removing:", team)
```

**Output**:
```
Team Member: Alice
Team Member: Bob
Team Member: Charlie
After Adding: ['Alice', 'Bob', 'Charlie', 'David']
After Removing: ['Alice', 'Charlie', 'David']
```

---

### **Topic 3: Working with Dictionaries**

Dictionaries are key-value pairs, widely used in data processing.

#### **Code Example**
```python
# Dictionary Example
employee = {
    "Name": "Alice",
    "Age": 30,
    "Role": "Engineer",
    "Salary": 75000
}

# Access values
print("Employee Name:", employee["Name"])

# Add new key-value pair
employee["Department"] = "Data Engineering"
print("Updated Dictionary:", employee)

# Loop through keys and values
for key, value in employee.items():
    print(key, ":", value)
```

---

### **Practice Task 1: Python Basics**
1. Create a Python script named `python_basics.py`.
2. Define:
   - Variables: a string, an integer, a float, and a boolean.
   - A list of numbers and find their sum using a loop.
   - A dictionary to store personal details like name, age, and role.
3. Print the values and use a loop to print the dictionary.

---

### **Next Steps**
Once this is done, we’ll move on to **functions, exception handling**, and **working with files** in Python, which will prepare us for real-world data engineering tasks.

Keep practicing! 🚀

### **Solution to Practice Task 1: Python Basics**

Here’s a complete solution to the practice task:

```python
# Variables
name = "John Doe"
age = 25
height = 5.9  # in feet
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# List of numbers and finding their sum
numbers = [10, 20, 30, 40, 50]
total = 0
for number in numbers:
    total += number
print("Sum of Numbers:", total)

# Dictionary to store personal details
personal_details = {
    "Name": "John Doe",
    "Age": 25,
    "Role": "Data Engineering Learner"
}

# Print values from the dictionary
print("Personal Details:")
for key, value in personal_details.items():
    print(f"{key}: {value}")
```

**Output:**
```
Name: John Doe
Age: 25
Height: 5.9
Is Student: True
Sum of Numbers: 150
Personal Details:
Name: John Doe
Age: 25
Role: Data Engineering Learner
```

---

## **Next Step: Functions, Exception Handling, and File Operations**

### **Topic 1: Functions**

Functions allow you to organize code into reusable blocks.

#### **Code Example**
```python
# Function to calculate the sum of a list of numbers
def calculate_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

# Using the function
numbers = [10, 20, 30, 40, 50]
print("Sum of Numbers:", calculate_sum(numbers))
```

---

### **Topic 2: Exception Handling**

Helps manage errors gracefully.

#### **Code Example**
```python
# Function to divide two numbers with exception handling
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed!"
    except TypeError:
        return "Error: Please provide numbers!"
    else:
        return result

print(divide_numbers(10, 2))  # Valid division
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, "a"))  # Invalid type
```

**Output:**
```
5.0
Error: Division by zero is not allowed!
Error: Please provide numbers!
```

---

### **Topic 3: File Operations**

Data engineers work heavily with files. Let's learn to **read** and **write** files.

#### **Code Example**
```python
# Write data to a file
with open("data.txt", "w") as file:
    file.write("Name,Age,Role\n")
    file.write("Alice,30,Engineer\n")
    file.write("Bob,25,Data Analyst\n")

# Read data from a file
with open("data.txt", "r") as file:
    content = file.readlines()
    for line in content:
        print(line.strip())
```

**Output:**
```
Name,Age,Role
Alice,30,Engineer
Bob,25,Data Analyst
```

---

### **Practice Task 2: Functions, Exception Handling, and File Operations**

1. Write a function `calculate_average` to compute the average of a list of numbers.
2. Write a program that:
   - Takes a list of numbers from the user.
   - Handles invalid input (e.g., entering a string instead of a number).
   - Saves the valid numbers to a file named `numbers.txt`.
   - Reads the numbers back from the file and calculates their average.

---

### **Solution to Practice Task 2: Functions, Exception Handling, and File Operations**

Here’s a complete solution for the task:

---

#### **Solution Code**

```python
# Function to calculate the average of a list of numbers
def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

# Function to get user input and validate it
def get_numbers_from_user():
    numbers = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ")
        if user_input.lower() == "done":
            break
        try:
            number = float(user_input)  # Convert input to a float
            numbers.append(number)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    return numbers

# Function to write numbers to a file
def write_numbers_to_file(numbers, filename):
    with open(filename, "w") as file:
        for number in numbers:
            file.write(f"{number}\n")

# Function to read numbers from a file
def read_numbers_from_file(filename):
    numbers = []
    with open(filename, "r") as file:
        for line in file:
            numbers.append(float(line.strip()))
    return numbers

# Main Program
filename = "numbers.txt"

# Step 1: Get numbers from user
print("Enter numbers to calculate their average. Type 'done' when finished.")
numbers = get_numbers_from_user()

# Step 2: Write numbers to a file
write_numbers_to_file(numbers, filename)
print(f"Numbers saved to {filename}.")

# Step 3: Read numbers from the file
read_numbers = read_numbers_from_file(filename)
print(f"Numbers read from file: {read_numbers}")

# Step 4: Calculate and display the average
average = calculate_average(read_numbers)
print(f"The average of the numbers is: {average}")
```

---

#### **Sample Run of the Program**

**Input/Output:**
```
Enter numbers to calculate their average. Type 'done' when finished.
Enter a number (or type 'done' to finish): 10
Enter a number (or type 'done' to finish): 20
Enter a number (or type 'done' to finish): abc
Invalid input! Please enter a valid number.
Enter a number (or type 'done' to finish): 30
Enter a number (or type 'done' to finish): done
Numbers saved to numbers.txt.
Numbers read from file: [10.0, 20.0, 30.0]
The average of the numbers is: 20.0
```

---

### **Explanation**

1. **`calculate_average(numbers)` Function**:
   - Computes the average of a list of numbers using `sum(numbers) / len(numbers)`.

2. **User Input Validation**:
   - Accepts input in a loop until the user types "done".
   - Converts valid inputs to floats and appends them to the list.
   - Catches invalid inputs using `try-except`.

3. **File Writing and Reading**:
   - Writes each number to a new line in the file `numbers.txt`.
   - Reads numbers back from the file and converts them to floats.

---


Here are **key and tricky points** that every Python and data engineering learner should keep in mind as they progress, along with examples to illustrate them.

---

### **1. Be Careful with Mutable Data Types**

- Lists, dictionaries, and sets are **mutable**, meaning changes to one reference affect all references.

#### **Example**
```python
# Mutable Example
list_a = [1, 2, 3]
list_b = list_a  # Both point to the same object
list_b.append(4)

print("list_a:", list_a)  # list_a is also modified
print("list_b:", list_b)
```

**Output:**
```
list_a: [1, 2, 3, 4]
list_b: [1, 2, 3, 4]
```

**Solution: Create a Copy Instead**
```python
list_a = [1, 2, 3]
list_b = list_a.copy()  # Create a shallow copy
list_b.append(4)

print("list_a:", list_a)  # Original remains unchanged
print("list_b:", list_b)
```

---

### **2. Efficient File Handling with Generators**

Processing large files efficiently is crucial in data engineering.

#### **Example**
```python
# Inefficient: Loads the entire file into memory
with open("large_file.txt", "r") as file:
    lines = file.readlines()

# Efficient: Reads one line at a time
with open("large_file.txt", "r") as file:
    for line in file:
        print(line.strip())  # Process each line
```

---

### **3. Avoid Hardcoding File Paths**

Use `os` or `pathlib` for portability.

#### **Example**
```python
import os

# Portable path handling
base_dir = os.path.dirname(os.path.abspath(__file__))  # Get current directory
file_path = os.path.join(base_dir, "data", "dataset.csv")

print("File Path:", file_path)
```

---

### **4. Use Logging Instead of Print Statements**

Logging is more robust and can be configured for different levels (e.g., DEBUG, INFO, ERROR).

#### **Example**
```python
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

logging.info("Processing data...")
logging.warning("Missing value encountered!")
logging.error("File not found!")
```

**Output:**
```
INFO: Processing data...
WARNING: Missing value encountered!
ERROR: File not found!
```

---

### **5. Handle Missing Data Gracefully**

When working with data, missing or invalid values are common.

#### **Example**
```python
import pandas as pd

# Sample data with missing values
data = {"Name": ["Alice", "Bob", None], "Age": [30, None, 25]}
df = pd.DataFrame(data)

# Fill missing values
df["Name"].fillna("Unknown", inplace=True)
df["Age"].fillna(df["Age"].mean(), inplace=True)

print(df)
```

**Output:**
```
     Name   Age
0   Alice  30.0
1     Bob  27.5
2  Unknown 25.0
```

---

### **6. Avoid Memory Issues with Large Datasets**

Use chunking to process large datasets efficiently.

#### **Example**
```python
import pandas as pd

# Process large CSV file in chunks
chunk_size = 1000
for chunk in pd.read_csv("large_dataset.csv", chunksize=chunk_size):
    print("Processing chunk...")
    print(chunk.head())
```

---

### **7. Leverage Python Libraries for Efficiency**

Don’t reinvent the wheel—use libraries like **Pandas, NumPy, PySpark**, etc., for complex tasks.

#### **Example: Using Pandas for Data Transformation**
```python
import pandas as pd

# Sample DataFrame
data = {"Name": ["Alice", "Bob", "Charlie"], "Age": [30, 25, 35]}
df = pd.DataFrame(data)

# Add a new column
df["Age in 5 Years"] = df["Age"] + 5

# Filter rows
filtered_df = df[df["Age"] > 30]

print(filtered_df)
```

---

### **8. Debug Code Effectively with `pdb`**

Use Python’s debugger to troubleshoot.

#### **Example**
```python
# Debugging Example
import pdb

def divide(a, b):
    pdb.set_trace()  # Start the debugger
    return a / b

result = divide(10, 0)  # Will raise ZeroDivisionError
```

---

### **9. Use SQL-Alike Syntax in Pandas**

For data engineers transitioning from SQL to Python, Pandas allows SQL-like operations.

#### **Example**
```python
import pandas as pd

# Sample DataFrame
data = {"Name": ["Alice", "Bob", "Charlie"], "Salary": [70000, 50000, 60000]}
df = pd.DataFrame(data)

# Query with a SQL-like filter
high_salary = df.query("Salary > 55000")

print(high_salary)
```

---

### **10. Write Efficient and Readable Code**

1. **List Comprehension**:
   ```python
   # Inefficient Loop
   squares = []
   for x in range(10):
       squares.append(x**2)

   # Efficient List Comprehension
   squares = [x**2 for x in range(10)]
   ```

2. **Use Enumerate Instead of Range**:
   ```python
   items = ["apple", "banana", "cherry"]

   for index, item in enumerate(items):
       print(f"{index}: {item}")
   ```

---

### **11. Optimize SQL Queries in Data Engineering**

When integrating Python with databases, optimize SQL queries for large datasets.

#### **Example: Query Optimization**
```python
import sqlite3

# Use LIMIT for large datasets
query = "SELECT Name, Age FROM employees WHERE Age > 30 LIMIT 1000"

connection = sqlite3.connect("database.db")
df = pd.read_sql_query(query, connection)
print(df)
```

---

### **12. Use Config Files for Parameters**

Avoid hardcoding parameters in scripts. Use `.env` or config files.

#### **Example**
```python
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Read environment variable
db_url = os.getenv("DATABASE_URL")
print("Database URL:", db_url)
```

---

### **Key Takeaways**
1. **Keep Code Modular**: Break tasks into reusable functions.
2. **Use Generators**: For large datasets to save memory.
3. **Automate Testing**: Use `pytest` or `unittest` to ensure code reliability.
4. **Secure Sensitive Data**: Use `.env` files for credentials.
5. **Understand the Ecosystem**: Familiarize yourself with libraries like Pandas, NumPy, PySpark, and tools like Hadoop and Kafka.

---

### **Next Steps**
Once you’ve understood and practiced this, we’ll move to the **Big Data section**, starting with **Hadoop Overview and History**, as outlined. Let me know when you’re ready! 🚀

Once you're done with the task or need help solving it! After this, we will move to **study cases for Big Data** from the outline. 🚀



# Comprehensive Guide to Module 2: Hadoop Ecosystem and Advanced Concepts

## Introduction to Hadoop
Hadoop is a powerful framework for distributed storage and processing of big data. This module focuses on HDFS, YARN, MapReduce, and integrations like Sqoop, Flume, and Hive, covering both theoretical and practical aspects.

---

## Section 1: HDFS (Hadoop Distributed File System)

### What is HDFS?
HDFS is a distributed storage system that splits files into blocks and distributes them across a cluster. It ensures fault tolerance by replicating blocks across multiple nodes.

### HDFS Architecture
1. **NameNode**: Stores metadata and manages the directory structure.
2. **DataNode**: Stores the actual file blocks.
3. **Secondary NameNode**: Merges logs to ensure NameNode efficiency.

### Read/Write Anatomy in HDFS
- **Write Operation**: The client writes a file, which is split into blocks and replicated across DataNodes.
- **Read Operation**: The client queries the NameNode for metadata and retrieves file blocks from DataNodes.

### Installing Hadoop and Setting Up HDFS

#### Steps to Install Hadoop
1. **Prerequisites**:
   - Install Java:
     ```bash
     sudo apt install openjdk-11-jdk
     ```
   - Download Hadoop:
     ```bash
     wget https://downloads.apache.org/hadoop/common/hadoop-3.3.5/hadoop-3.3.5.tar.gz
     tar -xzvf hadoop-3.3.5.tar.gz
     ```
2. **Configuration**:
   - Edit `core-site.xml` to set the default file system.
   - Edit `hdfs-site.xml` to configure replication and storage paths.

#### Starting HDFS Services
```bash
start-dfs.sh
```

### HDFS Commands

1. **Create a Directory**:
   ```bash
   hdfs dfs -mkdir /user/data
   ```
2. **Upload a File**:
   ```bash
   hdfs dfs -put localfile.txt /user/data
   ```
3. **List Files**:
   ```bash
   hdfs dfs -ls /user/data
   ```
4. **Read a File**:
   ```bash
   hdfs dfs -cat /user/data/localfile.txt
   ```
5. **Delete a File**:
   ```bash
   hdfs dfs -rm /user/data/localfile.txt
   ```

**Tip**: Use `-du -h` to monitor HDFS disk usage efficiently.

---

## Section 2: YARN and MapReduce

### What is YARN?
YARN (Yet Another Resource Negotiator) manages cluster resources and job scheduling. It separates resource management and job execution into:
1. **ResourceManager**: Allocates cluster resources.
2. **NodeManager**: Monitors node-level resources.

### Classical MapReduce Workflow
1. **Map Phase**: Splits input data into key-value pairs.
2. **Shuffle & Sort Phase**: Groups data by key.
3. **Reduce Phase**: Processes grouped data.

### Example: Word Count in MapReduce

#### Mapper Code (`mapper.py`):
```python
#!/usr/bin/env python3
import sys

for line in sys.stdin:
    words = line.strip().split()
    for word in words:
        print(f"{word}\t1")
```

#### Reducer Code (`reducer.py`):
```python
#!/usr/bin/env python3
import sys
from collections import defaultdict

word_counts = defaultdict(int)

for line in sys.stdin:
    word, count = line.strip().split("\t")
    word_counts[word] += int(count)

for word, count in word_counts.items():
    print(f"{word}\t{count}")
```

#### Running the Job
1. Upload input data to HDFS:
   ```bash
   hdfs dfs -put input.txt /user/data/input
   ```
2. Execute MapReduce:
   ```bash
   hadoop jar /path/to/hadoop-streaming.jar \
     -input /user/data/input \
     -output /user/data/output \
     -mapper mapper.py \
     -reducer reducer.py
   ```
3. View the Output:
   ```bash
   hdfs dfs -cat /user/data/output/part-00000
   ```

**Tips**:
- Use `Combiner` for local aggregation to improve performance.
- Use `Partitioner` for custom key grouping.

---

## Section 3: Integrating DBMS with Hadoop

### Setting Up MySQL
1. Install MySQL:
   ```bash
   sudo apt install mysql-server
   ```
2. Create a Database and Table:
   ```sql
   CREATE DATABASE sales;
   USE sales;
   CREATE TABLE orders (id INT, product_name VARCHAR(255), quantity INT);
   ```
3. Insert Sample Data:
   ```sql
   INSERT INTO orders VALUES (1, 'Laptop', 5), (2, 'Mouse', 10);
   ```

### Sqoop: Import/Export Data
1. **Import Data from MySQL to HDFS**:
   ```bash
   sqoop import --connect jdbc:mysql://localhost/sales \
     --username root --password password \
     --table orders --target-dir /user/data/orders
   ```
2. **Export Data from HDFS to MySQL**:
   ```bash
   sqoop export --connect jdbc:mysql://localhost/sales \
     --username root --password password \
     --table orders --export-dir /user/data/orders
   ```

---

## Section 4: Flume

### What is Flume?
Flume is used to ingest logs and streaming data into Hadoop.

### Setting Up Flume
1. Install Flume:
   ```bash
   sudo apt install flume-ng
   ```
2. Configure `flume.conf`:
   ```properties
   agent1.sources = source1
   agent1.sinks = sink1
   agent1.channels = channel1

   agent1.sources.source1.type = exec
   agent1.sources.source1.command = tail -f /var/log/syslog

   agent1.sinks.sink1.type = hdfs
   agent1.sinks.sink1.hdfs.path = hdfs://localhost:9000/user/flume/logs
   ```
3. Start Flume:
   ```bash
   flume-ng agent --conf /path/to/conf --name agent1 -Dflume.root.logger=INFO,console
   ```

---

## Section 5: Hive

### What is Hive?
Hive is a data warehouse infrastructure built on Hadoop for querying and analyzing data using SQL-like syntax.

### Hive Concepts
1. **Partitioning**: Organizes data into sub-directories.
2. **Bucketing**: Divides data into fixed-size chunks.

### Practical Example
1. **Create Hive Table**:
   ```sql
   CREATE TABLE games (name STRING, rating INT)
   ROW FORMAT DELIMITED
   FIELDS TERMINATED BY ','
   STORED AS TEXTFILE;
   ```
2. **Load Data**:
   ```sql
   LOAD DATA INPATH '/user/data/games.csv' INTO TABLE games;
   ```
3. **Query Data**:
   ```sql
   SELECT name, MAX(rating) AS top_rating FROM games GROUP BY name;
   ```

---

This article covers the theoretical and practical aspects of Module 2 with real-world, reusable examples. Let me know if you’d like to expand or refine any section!
