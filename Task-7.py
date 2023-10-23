### question 1
""" write a python program using  function which will do the following
    a) the function will create a text file with the current time stamp
    b) the file content should have the content of the current timestamp.
"""
## ans:

# datetime module give the date and time so import the datetime module
import datetime

def create_text_file_with_timestamp():
    # Get the current timestamp
    current_timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Create a file name with the current timestamp
    file_name = f"timestamp_{current_timestamp}.txt"

    # Open the file in write mode and create it if it doesn't exist
    with open(file_name, 'w') as file:
        file.write("This is a text file created with the current timestamp.")

    print(f"Text file '{file_name}' created successfully!")


# Call the function to create the text file with the current timestamp
create_text_file_with_timestamp()


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




