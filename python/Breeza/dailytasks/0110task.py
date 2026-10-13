users = [
    {"username": "aditya", "password": "1234"},
    {"username": "rohit", "password": "5678"},
    {"username": "ravi", "password": "abcd"},
    {"username": "amit", "password": "9876"},
    {"username": "sumit", "password": "pass123"}
]

username = input("Enter username: ")
password = input("Enter password: ")

login_success = False

for user in users:
    if user["username"] == username and user["password"] == password:
        login_success = True
        break

if login_success:
    print("Login successful!")
else:
    print("Invalid username or password!")
