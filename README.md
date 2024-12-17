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
Once you feel comfortable with basic Linux commands, let me know, and we will move to the next part of **Module 1**: **Setting Up Python Environment and Basics of Python Programming**.

