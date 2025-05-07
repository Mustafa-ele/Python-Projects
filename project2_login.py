#Simple Login & Registration System (with File Handling)

def register():
    username = input("Enter new username: ")
    password = input("Enter new password: ")

#Check if username already exists
    with open("users.txt", 'r') as f:
        for line in f:
            stored_user,_ = line.strip().split(',')
            if stored_user == username:
                print("Username already exists Try again ")
                return
            
    with open("users.txt", 'a') as f:
        f.write(f"{username},{password}\n")
    print("Registration successful!")

def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt",'r')as f:
        for line in f:
            if len(line.strip().split(',')) != 2:
                continue
            stored_user, stored_pass = line.strip().split(',')
            if stored_user == username and stored_pass == password:
                print("Login successful!🎉")
                return
    print("Invalid credentials")

#main menu
while True:
    print("\nWelcome")
    print("1.Register")
    print("2.Login")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        register()
    elif choice == '2':
        login()
    elif choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice, try again")