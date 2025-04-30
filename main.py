# user logs in
def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    with open("plain_text.txt", "r") as file:
        users = [line.strip().split(", ") for line in file.readlines()]
        for user, passw in users:
            if user == username and passw == password:
                print("Login successful!")
                new_menu()
                return
    print("Incorrect username or password. Try again.")

# register user
def register():
    while True:
        chosen_username = input("Choose a username: ")
        with open("plain_text.txt", "r") as file:
            users = [line.strip().split(", ")[0] for line in file.readlines()]
        if chosen_username in users:
            print("Username already taken. Try again.")
            continue

        chosen_password = input("Choose a password (minimum 4 characters): ")
        if len(chosen_password) < 4:
            print("Your password must be a minimum of 4 characters.")
            continue

        with open("plain_text.txt", "a") as file:
            file.write(f"{chosen_username}, {chosen_password}\n")
        print("Registration successful!")
        break

# quit option
def quit():
    exit()

def new_menu():
    print("1. Change password")
    print("2. Logout")
    log_or_change = input("What would you like to do? ")
    if log_or_change == 1:
        change_password()
    elif log_or_change == "2":
        print("Logged out.")
    else:
        print("Invalid input.")

#change password
def change_password():
    username = input("Enter your username: ")
    with open("plain_text.txt", "r") as file:
        users = [line.strip().split(", ") for line in file.readlines()]
    for i, (user, passw) in enumerate(users):
        if user == username:
            new_password = input("Enter a new password (minimum 4 characters): ")
            if len(new_password) < 4:
                print("Password too short.")
                return
            users[i][1] = new_password
            with open("plain_text.txt", "w") as file:
                for user, passw in users:
                    file.write(f"{user}, {passw}\n")
            print("Password changed successfully!")
            return
    print("Username not found.")

# User is offered a menu
def menu():
    print("1. Login")
    print("2. Register")
    print("3. Quit")
    selection = input("Select an option: ")
    if selection == "1":
        login()
    elif selection == "2":
        register()
    elif selection == "3":
        quit()
    else:
        print("Not a valid input.")

menu()