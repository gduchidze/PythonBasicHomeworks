import os
#1
def write_to_file(file):

    with open(file, 'w') as file:
        while True:
            user_input = input("Enter information for stop type 'n': ")

            if user_input.lower() == 'n':
                break

            file.write(user_input + '\n')

    print(f"Information has been transfered to  {file}.")


x = 'giorgiduchidze.txt'
write_to_file(x)

#2

def create_file():
    folder = input("Enter location: ")
    file_name = input("Enter filename: ")
    file_path = os.path.join(folder, file_name)

    with open(file_path, 'w') as file:
        file.write("This is a sample file content.")

    print(f"File '{file_name}' has been created at '{folder}'.")

    files = os.listdir(folder)
    print(f"List of files in '{folder}': {files}")

create_file()