# Problem Statement:  Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.
from logging import exception
from warnings import catch_warnings

try:
   with open("sample.txt", "r") as text1:
# print(text1.read())
# print(text1.readline())
# print(text1.readline())
# print(text1.readlines())
          for x in text1:
            print(x.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
     print(f"An excepted error occured! {e}")