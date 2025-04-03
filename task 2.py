# Problem Statement: Write a Python program that:
# 1.Takes user input and writes it to a file named output.txt.
# 2.Appends additional data to the same file.
# 3. Reads and displays the final content of the file.
with open("output.txt", "a") as text2:
    text2.write(" you have added content\n")
    text2.close()
# with open("output.txt", "w") as text2:
#     text2.write("hello there is not content!\n")
# text2.close()
with open("output.txt","r") as text2:
    print(text2.read())
