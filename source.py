"""
Student Management System with Analytics Dashboard
"""
import tkinter as tk                      # For GUI
from tkinter import messagebox            # For pop-up messages
import matplotlib.pyplot as plt           # For plotting graphs
import pandas as pd                       # For data manipulation

class app:
    #This block initializes the main window and calls the fucntion to make widgets on the screen
    def __init__(self,root):
        self.root = root
        self.root.geometry("400x400+600+200")                    
        self.root.configure(background="#010101")
        self.root.title("Student Management System")

        self.create_widgets()

    #This block clears all the widgets on the screen
    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    #The starting block of this program, it is called when the program starts, it is called in the constructor 
    def create_widgets(self):
        self.clear()
        self.root.geometry("400x400+600+200") #required for proper functioning of the program, it clears the screen before creating new widgets
        self.title = tk.Label(self.root, text="Student Management System",bg="#0b0f1a", fg="#e5e7eb", font=("", 14))
        self.title.pack(pady=20)

        self.login_button = tk.Button(self.root, text="Login", width=20,bg="#a78bfa", fg="black", activebackground="#8b5cf6", height=2,command=self.login_screen)
        self.login_button.pack(pady=10)

        self.signup_button = tk.Button(self.root, text="Sign Up", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6",command=self.signup_screen)
        self.signup_button.pack(pady=10)

        self.exit_button = tk.Button(self.root, text="Exit", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6",command=self.root.quit)
        self.exit_button.pack(pady=10)

    #This block creates the signup screen(GUI)
    def signup_screen(self):
        self.clear()
        self.title = tk.Label(self.root, text="Sign Up Screen", bg="#0b0f1a", fg="#e5e7eb")
        self.title.pack(pady=20)

        self.username_label = tk.Label(self.root, text="Username", bg="#0b0f1a", fg="#e5e7eb")
        self.username_label.pack()
        self.username = tk.Entry(self.root)
        self.username.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Password", bg="#0b0f1a", fg="#e5e7eb")
        self.password_label.pack()
        self.password = tk.Entry(self.root, show="*")
        self.password.pack(pady=5)

        self.role_label = tk.Label(self.root, text="Role", bg="#0b0f1a", fg="#e5e7eb")
        self.role_label.pack()
        self.role = tk.StringVar()
        self.role.set("Teacher")
        tk.Radiobutton(self.root, text="Teacher", variable=self.role, value="Teacher",bg="#0b0f1a", fg="#e5e7eb", selectcolor="#0b0f1a").pack()

        self.signup_button = tk.Button(self.root, text="Sign Up",bg="#a78bfa", fg="black", activebackground="#8b5cf6", width=20, height=2, command=self.signup)
        self.signup_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back",bg="#a78bfa", fg="black", activebackground="#8b5cf6", width=20, height=2, command=self.create_widgets)
        self.back_button.pack(pady=10)
    
    #Logic for signing up, it takes the username, password and role and saves it in a text file called users.txt
    def signup(self):
        username = self.username.get()
        password = self.password.get()
        role = self.role.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "Fields cannot be empty")
            return

        with open("users.txt", "a") as f:
            f.write(f"{username},{password},{role}\n")

        messagebox.showinfo("Success", "Account created!")
        self.create_widgets()

    #block for Login screen (GUI)
    def login_screen(self):
        self.clear()
        self.title = tk.Label(self.root, text="Login Screen", bg="#0b0f1a", fg="#e5e7eb", font=("Arial", 14))
        self.title.pack(pady=20)

        self.username_label = tk.Label(self.root, text="Username", bg="#0b0f1a", fg="#e5e7eb")
        self.username_label.pack()
        self.username = tk.Entry(self.root)
        self.username.pack(pady=5)

        self.password_label = tk.Label(self.root, text="Password", bg="#0b0f1a", fg="#e5e7eb")
        self.password_label.pack()
        self.password = tk.Entry(self.root, show="*")
        self.password.pack(pady=5)

        self.login_button = tk.Button(self.root, text="Login", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.login)
        self.login_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back",bg="#a78bfa", fg="black", activebackground="#8b5cf6", width=20, height=2, command=self.create_widgets)
        self.back_button.pack(pady=10)

    #This block is the logic for login
    def login(self):
        username = self.username.get()
        password = self.password.get()                  #it checks the users.txt file for the username and password
        try:                                           # if found it logs in the user and shows the dashboard according to the role of the user
            with open("users.txt", "r") as f:          # if not found it shows an error message        
                for line in f:
                    parts = line.strip().split(",")
                    u, p, role = parts

                    if u == username and p == password:
                        self.current_user = username
                        self.current_role = role
                        self.Dashboard(self.current_role)
                        return
            messagebox.showerror("Error", "Invalid username or password")

        except FileNotFoundError:
            messagebox.showerror("Error", "User file not found")


        #The main screen of the program after login, it shows different options according to the role of the user
    def Dashboard(self, role):
        self.clear()
        self.root.geometry("900x800+300+50")
        self.title = tk.Label(self.root, text=f"Welcome {role}", bg="#0b0f1a", fg="#e5e7eb", font=("Arial", 14))
        self.title.pack(pady=20)

        if role == "Student":
            self.info_label = tk.Label(self.root, text="Student Dashboard", bg="#0b0f1a", fg="#e5e7eb")
            self.info_label.pack(pady=10)

            self.view_grades_button = tk.Button(self.root, text="View Grades", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.view_grades)
            self.view_grades_button.pack(pady=10)

            self.view_details_button = tk.Button(self.root, text="View Details", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.view_student_details)
            self.view_details_button.pack(pady=10)

            self.view_eca_button = tk.Button(self.root, text="View ECA", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.view_eca)
            self.view_eca_button.pack(pady=10)

            self.update_password_button = tk.Button(self.root, text="Update Password", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.change_password_screen)
            self.update_password_button.pack(pady=10)

            self.logout_button = tk.Button(self.root, text="Logout", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.create_widgets)
            self.logout_button.pack(pady=10)

        else:
            self.info_label = tk.Label(self.root, text="Teacher Dashboard", bg="#0b0f1a", fg="#e5e7eb")
            self.info_label.pack(pady=10)

            self.add_student_button = tk.Button(self.root, text="Add Student", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.add_student_screen)
            self.add_student_button.pack(pady=10)

            self.delete_student_button = tk.Button(self.root, text="Delete Student", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.delete_student_screen)
            self.delete_student_button.pack(pady=10)

            self.view_details_button = tk.Button(self.root, text="View Student List", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.view_student_details_teacher)
            self.view_details_button.pack(pady=10)

            self.Add_grades_button = tk.Button(self.root, text="Add Grades", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.add_grades_screen)
            self.Add_grades_button.pack(pady=10)

            self.view_grades_button = tk.Button(self.root, text="View Grades", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.view_grades)
            self.view_grades_button.pack(pady=10)

            self.add_eca_button = tk.Button(self.root, text="Add ECA", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.add_eca_screen)
            self.add_eca_button.pack(pady=10)

            self.view_eca_button = tk.Button(self.root, text="View ECA", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.view_eca)
            self.view_eca_button.pack(pady=10)

            self.insights_button = tk.Button(self.root, text="View Insights", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.Analytic_Dashboard)
            self.insights_button.pack(pady=10)

            self.logout_button = tk.Button(self.root, text="Logout", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.create_widgets)
            self.logout_button.pack(pady=10)

            

        #------------------Add Student Block-------------------

        #This block is for adding a student (GUI)
    def add_student_screen(self):
        self.clear()

        self.student_username_label = tk.Label(self.root, text="Username:", bg="#0b0f1a", fg="#e5e7eb")
        self.student_username_label.pack(pady=10)

        self.student_username = tk.Entry(self.root)
        self.student_username.pack(pady=10)

        self.add_student_button = tk.Button(self.root, text="Add Student", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.add_student)
        self.add_student_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=lambda: self.Dashboard(self.current_role))
        self.back_button.pack(pady=10)

        #This block takes the username of the student and save it in the users.txt file with a default password and role as student
    def add_student(self):
        username = self.student_username.get()

        if not username:
                messagebox.showerror("Error", "Enter username")
                return

        with open("users.txt", "a") as f:
                f.write(f"{username},123,Student\n")

        messagebox.showinfo("Success", "Student created (password: 123)")
                        
        #------------------Update password Block-------------------

        #This block is for changing the password of the user (GUI)
    def change_password_screen(self):
        self.clear()

        tk.Label(self.root, text="Change Password",bg="#0b0f1a", fg="#e5e7eb").pack(pady=20)

        tk.Label(self.root, text="New Password",bg="#0b0f1a", fg="#e5e7eb").pack()

        self.new_password = tk.Entry(self.root, show="*")
        self.new_password.pack()

        tk.Button(self.root, text="Update", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.update_password).pack(pady=10)

        tk.Button(self.root, text="Back", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=lambda: self.Dashboard(self.current_role)).pack()

        #This block updates the password of the user in the users.txt file by reading the file, updating the password for the current user and writing it back to the file
    def update_password(self):
        new_pass = self.new_password.get()

        if not new_pass:
            messagebox.showerror("Error", "Enter password")
            return

        lines = []

        try:
            with open("users.txt", "r") as f:
                for line in f:
                    u, p, r = line.strip().split(",")

                    if u == self.current_user:
                        lines.append(f"{u},{new_pass},{r}\n")
                    else:
                        lines.append(line)
        except FileNotFoundError:
            messagebox.showerror("Error", "User file not found")
            return

        with open("users.txt", "w") as f:
            f.writelines(lines)

        messagebox.showinfo("Success", "Password updated!")
        self.Dashboard(self.current_role)

        #------------------Add ECA Block-------------------
        #this block is for adding ECA activity for a student (GUI)
    def add_eca_screen(self):
        self.clear()

        tk.Label(self.root, text="Add ECA Activity", bg="#0b0f1a", fg="#e5e7eb", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Student Username:", bg="#0b0f1a", fg="#e5e7eb").pack()
        self.eca_user = tk.Entry(self.root)
        self.eca_user.pack(pady=5)

        tk.Label(self.root, text="Activity:", bg="#0b0f1a", fg="#e5e7eb").pack()
        self.act_entry = tk.Entry(self.root)
        self.act_entry.pack(pady=5)

        tk.Label(self.root, text="Hours per Week:", bg="#0b0f1a", fg="#e5e7eb").pack()
        self.hours_entry = tk.Entry(self.root)
        self.hours_entry.pack(pady=5)

        tk.Button(self.root, text="Save", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.save_eca).pack(pady=10)

        tk.Button(self.root, text="Back", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6",command=lambda: self.Dashboard(self.current_role)).pack(pady=10)

        #this block saves the ECA activity for the student in a text file called eca.txt in the format username,activity,hours
    def save_eca(self):
        username = self.eca_user.get()
        activity = self.act_entry.get()
        hours = self.hours_entry.get()

        if not username or not activity or not hours:
            messagebox.showerror("Error", "All fields required")
            return

        lines = []
        found = False

        try:
            with open("eca.txt", "r") as f:
                for line in f:
                    data = line.strip().split(",")

                    if data[0] == username:
                        lines.append(f"{username},{activity},{hours}\n")
                        found = True
                    else:
                        lines.append(line)
        except FileNotFoundError:
            pass

        if not found:
            lines.append(f"{username},{activity},{hours}\n")

        with open("eca.txt", "w") as f:
            f.writelines(lines)

        messagebox.showinfo("Success", "ECA saved!")

        #------------------Add Grades Block-------------------

        #This block is for adding grades for a student(GUI)
    def add_grades_screen(self):
        self.clear()

        tk.Label(self.root, text="Add Grades", bg="#0b0f1a", fg="#e5e7eb", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.root, text="Student Username:", bg="#0b0f1a", fg="#e5e7eb").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack(pady=5)

        subjects = ["AE & EC", "FODS", "FOM", "IT", "MFC"]
        self.marks_entries = []

        for sub in subjects:
            tk.Label(self.root, text=sub, bg="#0b0f1a", fg="#e5e7eb").pack()
            e = tk.Entry(self.root)
            e.pack(pady=5)
            self.marks_entries.append(e)

        tk.Button(self.root, text="Save", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.save_grades).pack(pady=10)
        tk.Button(self.root, text="Back", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=lambda: self.Dashboard(self.current_role)).pack(pady=10)

        #this block saves the grades for the student in a text file called grades.txt in the format username,mark1,mark2,mark3,mark4,mark5
    def save_grades(self):
        username = self.username_entry.get()

        if username == "":
            messagebox.showerror("Error", "Enter username")
            return

        try:
            marks = []

            for entry in self.marks_entries:
                value = entry.get()

                if value == "":
                    messagebox.showerror("Error", "Fill all marks")
                    return

                marks.append(int(value))  

            lines = []
            found = False

            try:
                with open("grades.txt", "r") as f:
                    for line in f:
                        data = line.strip().split(",")

                        if data[0] == username:
                            lines.append(f"{username},{marks[0]},{marks[1]},{marks[2]},{marks[3]},{marks[4]}\n")
                            found = True
                        else:
                            lines.append(line)
            except FileNotFoundError:
                pass

            if not found:
                lines.append(f"{username},{marks[0]},{marks[1]},{marks[2]},{marks[3]},{marks[4]}\n")

            with open("grades.txt", "w") as f:
                f.writelines(lines)

            messagebox.showinfo("Success", "Grades saved!")

        except:
            messagebox.showerror("Error", "Enter valid numbers")

     #----------------------Delete Student Block-------------------

        #this block is for deleting a student from the system (GUI)
    def delete_student_screen(self):
        self.clear()

        tk.Label(self.root, text="Delete Student", bg="#0b0f1a", fg="#e5e7eb", font=("Arial", 14)).pack(pady=20)

        tk.Label(self.root, text="Student Username:", bg="#0b0f1a", fg="#e5e7eb").pack()
        self.del_username_entry = tk.Entry(self.root)
        self.del_username_entry.pack(pady=5)

        tk.Button(self.root, text="Delete", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=self.delete_student).pack(pady=10)
        tk.Button(self.root, text="Back", width=20, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=lambda: self.Dashboard(self.current_role)).pack(pady=10)

        #this block deletes the student from the users.txt file by reading the file, removing the line with the username and writing it back to the file
    def delete_student(self):
        username = self.del_username_entry.get()

        if username == "":
            messagebox.showerror("Error", "Enter username")
            return

        lines = []

        try:
            with open("users.txt", "r") as f:
                for line in f:
                    u, p, r = line.strip().split(",")

                    if u != username or r != "Student":
                        lines.append(line)

            with open("users.txt", "w") as f:
                f.writelines(lines)

            messagebox.showinfo("Success", "Student deleted!")

        except FileNotFoundError:
            messagebox.showerror("Error", "User file not found")
        
     #------------------View Student Details Block-------------------

        #this block is for viewing the details of the student, it shows the username, password and role of the student (GUI)
    def view_student_details(self):
        self.clear()

        tk.Label(self.root, text="My Details", bg="#0b0f1a", fg="#e5e7eb").pack(pady=20)

        self.detail_text = tk.Text(self.root, bg="#0b0f1a", fg="#e5e7eb", height=10, width=40)
        self.detail_text.pack(pady=10)

        tk.Button(self.root,text="Back",bg="#a78bfa", fg="black", activebackground="#8b5cf6",command=lambda: self.Dashboard(self.current_role)).pack(pady=10)

        try:
            with open("users.txt", "r") as f:
                for l in f:
                    u, p, r = l.strip().split(",")

                    if u == self.current_user:
                        self.detail_text.insert("end",f"Username: {u}\nPassword: {p}\nRole: {r}")
                        self.detail_text.config(state="disabled")  # read-only
                        return

            self.detail_text.insert("end", "User not found")
            self.detail_text.config(state="disabled")

        except FileNotFoundError:
            self.detail_text.insert("end", "User file not found")
            self.detail_text.config(state="disabled")

        
        #this block is for viewing the details of all the students, it shows the username and password of all the students (GUI)
    def view_student_details_teacher(self):
        self.clear()

        tk.Label(self.root,text="All Student Details",bg="#0b0f1a",fg="#e5e7eb",font=("", 12)).pack(pady=20)

        self.detail_text = tk.Text(self.root, bg="#0b0f1a", fg="#e5e7eb", height=15, width=50)
        self.detail_text.pack(pady=10)

        try:
            with open("users.txt", "r") as f:
                found = False
                for l in f:
                    u, p, r = l.strip().split(",")
                    if r == "Student":
                        found = True
                        self.detail_text.insert(
                            "end",
                            f"Username: {u}\nPassword: {p}\n-------------------\n"
                        )

                if not found:
                    self.detail_text.insert("end", "No students found")

            self.detail_text.config(state="disabled")

        except FileNotFoundError:
            self.detail_text.insert("end", "User file not found")
            self.detail_text.config(state="disabled")

        tk.Button(self.root,text="Back",bg="#a78bfa", fg="black", activebackground="#8b5cf6",command=lambda: self.Dashboard(self.current_role)).pack(pady=10)

        #------------------View Grades & ECA Block-------------------
        #this block is for viewing the grades of the student, it shows the grades of all the subjects for the student (GUI)
    def view_grades(self):
        self.clear()

        tk.Label(self.root, text="All Students Grades", bg="#0b0f1a", fg="#e5e7eb").pack(pady=20)

        text_box = tk.Text(self.root, width=70, height=18, bg="#0b0f1a", fg="#e5e7eb")
        text_box.pack(pady=10)

        try:
            found = False

            with open("grades.txt", "r") as f:
                for l in f:
                    data = l.strip().split(",")

                    if len(data) == 6:
                        username = data[0]
                        marks = data[1:]

                        text_box.insert("end", "Student: " + username + "\n")

                        text_box.insert("end", "AE & EC = " + marks[0] + "\n")
                        text_box.insert("end", "FODS = " + marks[1] + "\n")
                        text_box.insert("end", "FOM = " + marks[2] + "\n")
                        text_box.insert("end", "IT = " + marks[3] + "\n")
                        text_box.insert("end", "MFC = " + marks[4] + "\n")

                        text_box.insert("end", "\n----------------------\n")

                        found = True

            if not found:
                text_box.insert("end", "No grades found!")

        except FileNotFoundError:
            text_box.insert("end", "Grades file not found!")

        text_box.config(state="disabled")

        tk.Button(self.root, text="Back",bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=lambda: self.Dashboard(self.current_role)).pack(pady=10)
    
        #this block is for viewing the ECA activities of the student, it shows the activity and hours per week for the student (GUI)
    def view_eca(self):
        self.clear()

        tk.Label(self.root, text="Student ECA Records", bg="#0b0f1a", fg="#e5e7eb", font=("Arial", 14)).pack(pady=20)

        text_box = tk.Text(self.root, width=70, height=18, bg="#0b0f1a", fg="#e5e7eb")
        text_box.pack(pady=10)

        try:
            found = False

            with open("eca.txt", "r") as f:
                for l in f:
                    data = l.strip().split(",")

                    if len(data) == 3:
                        username = data[0]
                        activity = data[1]
                        hours = data[2]

                        text_box.insert("end", "Student: " + username + "\n")
                        text_box.insert("end", "Activity = " + activity + "\n")
                        text_box.insert("end", "Hours per Week = " + hours + "\n")
                        text_box.insert("end", "\n----------------------\n")

                        found = True

            if not found:
                text_box.insert("end", "No ECA records found!")

        except FileNotFoundError:
            text_box.insert("end", "ECA file not found!")

        text_box.config(state="disabled")

        tk.Button(self.root, text="Back",bg="#a78bfa", fg="black", activebackground="#8b5cf6", command=lambda: self.Dashboard(self.current_role)).pack(pady=10)

          #------------------Analytic_Dashboard-------------------

        #this block is for the analytics dashboard, it shows three options for the teacher to view the grade trends, ECA impact and performance alerts (GUI)
    def Analytic_Dashboard(self):
    
        self.clear()

        tk.Label(self.root, text="📊 Analytics Dashboard",bg="#0b0f1a", fg="#e5e7eb").pack(pady=20)

        tk.Button(self.root, text="📈 Grade Trends",width=25, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6",command=self.grade_trends_screen).pack(pady=10)

        tk.Button(self.root, text="🔗 ECA Impact",width=25, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6",command=self.eca_impact_screen).pack(pady=10)

        tk.Button(self.root, text="⚠ Performance Alerts",width=25, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6",command=self.performance_alerts_screen).pack(pady=10)

        tk.Button(self.root, text="Back",width=25, height=2,bg="#a78bfa", fg="black", activebackground="#8b5cf6",command=lambda: self.Dashboard(self.current_role)).pack(pady=20)

        # This block is for viewing the grade trends of the students,
        # it shows a bar graph comparing the grades of all the students in different subjects 
        # It also shows the average grade of each student (GUI + Graph)
    def grade_trends_screen(self):
        try:
            records = []

            with open("grades.txt", "r") as f:
                for l in f:
                    data = l.strip().split(",")

                    if len(data) != 6:
                        continue

                    records.append({
                        "username": data[0],
                        "AE_EC": int(data[1]),
                        "FODS": int(data[2]),
                        "FOM": int(data[3]),
                        "IT": int(data[4]),
                        "MFC": int(data[5])
                    })

            if not records:
                messagebox.showinfo("Info", "No grade records found")
                return

            df = pd.DataFrame(records)

            df["Average"] = df[["AE_EC", "FODS", "FOM", "IT", "MFC"]].mean(axis=1)

            # ---------------- UI WINDOW ----------------
            top = tk.Toplevel(self.root)
            top.title("Grade Trends")
            top.geometry("700x500")

            tk.Label(top, text="Grade Trends").pack(pady=10)

            # text display of the grades and average for each student
            text_box = tk.Text(top, bg="#0b0f1a", fg="#e5e7eb")
            text_box.pack(fill="both", expand=True)
            text_box.insert("end", df.to_string(index=False))
            text_box.config(state="disabled")

            # ---------------- GRAPH ----------------
            plt.figure(figsize=(6, 4))

            df.set_index("username")[["AE_EC", "FODS", "FOM", "IT", "MFC"]].plot(kind="bar")

            plt.title("Student Grade Comparison")
            plt.ylabel("Marks")
            plt.xticks(rotation=45)
            plt.tight_layout()

            plt.show()

        except FileNotFoundError:
            messagebox.showerror("Error", "grades.txt not found")
        
        # This block is for analyzing the impact of ECA on the academic performance of the students,
        # It shows a scatter plot with ECA hours on x-axis and average marks on y-axis,
        # It also shows a text display of the ECA hours and average marks for each student (GUI + Graph)

    def eca_impact_screen(self):
        try:
            eca_data = {}

            with open("eca.txt", "r") as f:
                for l in f:
                    data = l.strip().split(",")
                    username = data[0]
                    hours = int(data[2])

                    eca_data[username] = hours

            records = []

            with open("grades.txt", "r") as f:
                for l in f:
                    data = l.strip().split(",")

                    if len(data) != 6:
                        continue

                    username = data[0]

                    avg = sum(map(int, data[1:])) / 5

                    records.append({
                        "username": username,
                        "average": avg,
                        "eca_hours": eca_data.get(username, 0)
                    })

            if not records:
                messagebox.showinfo("Info", "No data available")
                return

            df = pd.DataFrame(records)


            top = tk.Toplevel(self.root)
            top.title("ECA Impact Analysis")
            top.geometry("700x500")

            tk.Label(top, text="🔗 ECA Impact on Performance",
                    font=("Arial", 14, "bold")).pack(pady=10)


            text_box = tk.Text(top, bg="#0b0f1a", fg="#e5e7eb")
            text_box.pack(fill="both", expand=True)

            text_box.insert("end", df.to_string(index=False))

            text_box.config(state="disabled")


            plt.figure(figsize=(6, 4))

            plt.scatter(df["eca_hours"], df["average"])

            plt.title("ECA Hours vs Academic Performance")
            plt.xlabel("ECA Hours per Week")
            plt.ylabel("Average Marks")

            plt.grid(True)

            plt.show()

        except FileNotFoundError:
            messagebox.showerror("Error", "Missing eca.txt or grades.txt")

        # This block is for generating performance alerts based on the average marks of the students,
        # It categorizes students into three groups: weak (<50), average (50-75) and good (>75) 
        # It displays the list of students in each category (GUI)

    def performance_alerts_screen(self):
        try:
            records = []

            with open("grades.txt", "r") as f:
                for l in f:
                    data = l.strip().split(",")
                    username = data[0]
                    marks = list(map(int, data[1:]))

                    avg = sum(marks) / 5

                    records.append({
                        "username": username,
                        "average": avg
                    })

            if not records:
                messagebox.showinfo("Info", "No grade data found")
                return


            weak = []
            average = []
            good = []

            for r in records:
                if r["average"] < 50:
                    weak.append(r)
                elif r["average"] <= 75:
                    average.append(r)
                else:
                    good.append(r)


            top = tk.Toplevel(self.root)
            top.title("Performance Alerts")
            top.geometry("600x500")

            tk.Label(top, text="Performance Alerts",
                    font=("Arial", 14, "bold")).pack(pady=10)

            text_box = tk.Text(top, bg="#0b0f1a", fg="#e5e7eb")
            text_box.pack(fill="both", expand=True)

            # ---------------- DISPLAY ----------------
            text_box.insert("end", " WEAK STUDENTS (<50)\n")
            for s in weak:
                text_box.insert("end", f"{s['username']} - {s['average']:.2f}\n")

            text_box.insert("end", "\n AVERAGE STUDENTS (50-75)\n")
            for s in average:
                text_box.insert("end", f"{s['username']} - {s['average']:.2f}\n")

            text_box.insert("end", "\n GOOD STUDENTS (>75)\n")
            for s in good:
                text_box.insert("end", f"{s['username']} - {s['average']:.2f}\n")

            text_box.config(state="disabled")

        except FileNotFoundError:
            messagebox.showerror("Error", "grades.txt not found")
  

root = tk.Tk()
app(root)
root.mainloop()

