u1 = []
u2 = []
u3 = []

print("User 1: ")
u1 = [input("Enter Your Name"), input("Enter Your LastName"), int(input("Enter Your Age"))]
print("\nUser 2: ")
u2 = [input("Enter Your Name"), input("Enter Your LastName"), int(input("Enter Your Age"))]
print("\nUser 3: ")
u3 = [input("Enter Your Name"), input("Enter Your LastName"), int(input("Enter Your Age"))]

consumer_info = [u1, u2, u3]
print("\nCombined User Information:")

for i, u in enumerate(consumer_info, 1):
    print(f"User {i} - Name: {u[0]}, Lastname: {u[1]}, Age: {u[2]}")
while True:
    try:
        index = int(input("\nEnter the user index for information (1-3) or enter 0 to exit "))
        if index == 0:
            break
        elif 1 <= index <= 3:
            x = consumer_info[index - 1]
            print(f"Name: {x[0]}, Lastname: {x[1]}, Age: {x[2]}")
        else:
            print("Invalid index.enter a number between 1 and 3.")
    except ValueError:
        print("Please enter a valid number.")




user_data = {}

print("Registration:")
name = input("Enter your name: ")
password = input("Enter your password (must be more than 8 characters): ")

if name == "" and len(password) > 8:
    user_data["name"] = name
    user_data["password"] = password
    print("Registration successful!")
else:
    print("Invalid registration. Name field must be empty, and password must be more than 8 characters.")

print("\nLogin:")
name1 = input("Enter your name: ")
password1 = input("Enter your password: ")

if name1 == user_data.get("name") and password1 == user_data.get("password"):
    print("Login successful! Welcome back, {}!".format(name1))
else:
    print("Login failed. Please check your entered information.")
