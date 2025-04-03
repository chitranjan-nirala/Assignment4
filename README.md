# **Module 5: Files, Exceptions, and Errors in Python**

## **Overview**  
This module covers file handling in Python, including reading, writing, appending data, and handling errors gracefully using exceptions.

---

## **Task 1: Read a File and Handle Errors**  

### **Problem Statement**  
Write a Python program that:  
1. Opens and reads a text file named `sample.txt`.  
2. Prints its content line by line.  
3. Handles errors gracefully if the file does not exist.  

### **Expected Output**  

#### ✅ If the file exists:
```
Hello, this is line 1.
This is line 2.
Welcome to file handling in Python!
```

#### ❌ If the file does not exist:
```
Error: The file 'sample.txt' was not found.
```

### **Implementation Details**  
- Use `with open()` to safely open and close the file.  
- Use exception handling (`try-except`) to manage missing files.  
- Use `.strip()` to clean up extra whitespace when printing lines.  

---

## **Task 2: Write and Append Data to a File**  

### **Problem Statement**  
Write a Python program that:  
1. Takes user input and writes it to a file named `output.txt`.  
2. Appends additional data to the same file.  
3. Reads and displays the final content of the file.  

### **Expected Output**  

For example, if the user enters:  
```
Enter text: Python is awesome!
Enter text: I love coding.
```

#### **Content of `output.txt` after execution:**  
```
Python is awesome!
I love coding.
```

### **Implementation Details**  
- Use `open("output.txt", "w")` to write user input to a file.  
- Use `open("output.txt", "a")` to append new input without overwriting previous data.  
- Use `open("output.txt", "r")` to read and print the final content.  

---

## **How to Run the Programs**  
1. Save the Python scripts (`task1.py` and `task2.py`) in the same directory as this README file.  
2. Run the scripts using Python:  
   ```bash
   python task1.py
   python task2.py
   ```
3. Follow the prompts and observe the output.

---

## **Key Learning Outcomes**  
✔ Understanding file handling (`r`, `w`, `a` modes).  
✔ Implementing exception handling (`try-except`).  
✔ Reading, writing, and appending files in Python.  

---

### **Author**  
[Your Name]  
