### question 1
""" write a python program using  function which will do the following
    a) the function will create a text file with the current time stamp
    b) the file content should have the content of the current timestamp.
"""
## ans:
# import datetime module 
import datetime

def fun():
    f = open("guvi.txt", "w")
    print(f.name)
    if f.name == "guvi.txt":
        x = datetime.datetime.now()
        f.write(f'Current date and time: " + {x}')   # create a file with curent time stamp
        f.close()  # Don't forget to close the file after writing
        print("Current date and time written to the file.")
    else:
        print("Error")

fun()


## question 2
""" write a python function to read from a text file.The 
functiom will take the name of the text file and display
 the content of the file into the console"""
## ans:

def read_text_file(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        print(f"File not found: {file_name}")

# Enter a file path
file_name = r"Task.txt.txt"
read_text_file(file_name)




