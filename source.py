# THIS IS WHERE WE WILL WRITE CODE
# lets complete our assignment this week by next tuesday and learn 
# till filehandling then we will begin and try to complete in the reamaing time
#preferably 3 days then lasting if time remains we  could try to implement that library 
#for 10 extra points  
# make sure to clone my repository and remote connect this repositty to your local 
# repository 


#Student management system

def sign_up():
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    with open("database.txt", "a") as f:
        f.write(username + ", " + password + "\n")
    print(f"Saved {username} successfully!")

def log_in():
    username = input("Enter Your username: ")
    password = input("Enter your password: ")
    found = False
    try:
        with open("database.txt", "r") as f:
            for l in f:
                saved_user, saved_pass = l.strip().split(", ")  # Strip removes any whitespaces
                if username == saved_user and password == saved_pass:
                    print(f"Log in successful {username}!")
                    found = True
                    break
            if not found:
                print("Invalid username or password!")
                
    except FileNotFoundError:
        print("File not found!")

def clear_database():
    with open("database.txt", "w") as f:
        pass  #overwrite nothing
    print("All data cleared!")  

while True:

    print("\nHere are a bunch of operations u can execute:")
    print("1. Sign up")
    print("2. Log in")
    print("3. clear database")
    print("4. Exit")

    x = int(input("Choose any number: "))

    if x == 1:
        sign_up()
    elif x == 2:
        log_in()
    elif x == 3:
        clear_database()
    elif x == 4:
        break


