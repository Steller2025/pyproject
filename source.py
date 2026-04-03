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
    role = input("Enter Role: ")
    with open("database.txt", "a") as f:
        f.write(username + ", " + password + ", " + role + "\n")
    return f"Saved {username} successfully!"

def log_in():
    username = input("Enter Your username: ")
    password = input("Enter your password: ")
    try:
        with open("database.txt", "r") as f:
            for l in f:
                saved_user, saved_pass, role = l.strip().split(", ")  # Strip removes any whitespaces
                if username == saved_user and password == saved_pass:
                    return f"Log in successful {username}!", role, username
            return "Invalid username or password!"
                
    except FileNotFoundError:
        return "File not found!"
    
def view_grades(username):
    try:
        with open("grades.txt", "r") as f:
            for l in f:
                data = l.strip().split(", ")  # Data becomes a list

                if data[0] == username:
                    return f"Your grades: {data[1:]}"

        return f"No grades found!" 
    except FileNotFoundError:
        return f"Grade file not found!"
    
def view_eca(username):
    try:
        with open("eca.txt", "r") as f:
            for l in f:
                data = l.strip().split(", ")

                if data[0] == username:
                    return f"Your ECA: {data[1:]}"
                
        return f"No ECA found!"
    except FileNotFoundError:
        return f"ECA file not found!"
    
def add_students():
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    
    with open("database.txt", "a") as f:
        f.write(f"{username}, {password}, student\n")

    return f"Student added successfully!"

def delete_students():
    pass
    
def Admin_Panel(username):
    while True:
        print("Admin Panel")
        print("1. Add Student")
        print("2. Delete Student")
        print("3. View All Student")
        print("4. Average Grade")
        print("5. Go Back")
        print("6. Exit")

        try:
            z = int(input("Choose any option: "))
        except ValueError:
            print("Enter a valid Number!")
            continue
        
        if z == 1:
            add_students()

        elif z == 2:
            print(delete_students())

        elif z == 3:
            print(view_all_student(username))

        elif z == 4:
            print(average_grade(username))
        
        elif z == 5:
            break

        elif z == 6:
            exit()

        else:
            print("Invalid Option!")
            
def Student_Panel(username):
    while True:
        print("Student_Panel")
        print("1. View Grades")
        print("2. View ECA")
        print("3. Go Back")
        print("4. Exit")

        try:
            y = int(input("Choose any option: "))
        except ValueError:
            print("Enter a valid number!")
            continue

        if y == 1:
            print(view_grades(username))
        elif y == 2:
            print(view_eca(username))
        elif y == 3:
            break
        elif y == 4:
            exit()
        else:
            print("Invalid Option!")
    
while True:

    print("\nHere are a bunch of operations u can execute:")
    print("1. Sign up")
    print("2. Log in")
    print("3. Exit")
    
    try:
        x = int(input("Choose any number: "))
    except ValueError:
        print("Enter a valid number!")
        continue

    if x == 1:
        print(sign_up())
    elif x == 2:
        result = log_in()
        if result == "Invalid username or password!" or result == "File not found!":
            print(result)
        else:
            message, role, user = result
            print(message)

            if role.lower() == "admin":
                print("Welcome Admin!")
                Admin_Panel(user)

            elif role.lower() == "student":
                print("Welcome Student!")
                Student_Panel(user)
            else:
                print("Sth error happened!")
    elif x == 3:
        break
    else:
        print("Invalid Choice!")
