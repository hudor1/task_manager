# The program works with two text files, 'user.txt' and 'tasks.txt'.
# The usernames and passwords are saved in 'user.txt' while tasks information
# such as task title, task description, task due date are saved in 'tasks.txt'.
# Only the admin is able to register new users and only the admin has a statistics menu
# that prints out total users and total tasks.
# The signed on user is able to view all tasks including their own tasks by selecting
# the correct options.

#=====importing libraries===========
'''This is the section where you will import libraries'''
import string
from datetime import datetime

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file
    - Use a while loop to validate your user name and password
'''


def login():    
    contents = "" 
    with open("user.txt", "r") as f:
        contents = f.readlines()
    
    usernames = []
    passwords = []
    
    for items in contents:
        item1, item2 = items.split(", ")
        item2 = item2.strip()
        usernames.append(item1)
        passwords.append(item2)
    # Usernames and passwords lists are converted to a dictionary.
    user_credentials = dict(zip(usernames,passwords))
    
    print()   
    while True:
        # The username variable is converted to a universal variable so that it can be shared with other functions; "signed_on_user" in this instance.
        global username
        username = input("Enter username: ").strip()
        username = username.split()
        username = "".join(username)    
        
        password = input("Enter password: ")
        # Checks if the username exists in the user_credentials dictionary.
        if username not in user_credentials:
             print("Username does not exist")
        # If the username exists but the password is incorrect, the user is prompted to enter the password again.   
        elif username in user_credentials and password != user_credentials[username]:
            print("Invalid password!")
                
        else:
            # If the username and passwords correspond, the user is logged in.
            username in user_credentials and password == user_credentials[username]              
            break

login()

# Takes on the username of the signed on user.
signed_on_user = []
signed_on_user.append(username)
signed_on_user = "".join(signed_on_user)
print(f"Welcome {signed_on_user} ")
print()

# Creates a menu with view statistics that's only available for admin user.
while True:
    if signed_on_user == "admin":
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
vs - view statistics                    
e - exit
: ''').lower()
        
    else:
        # Present the menu to the user and 
        # make sure that the user input is converted to lower case.
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
e - exit
: ''').lower()

    if menu == 'r':
        
        '''This code block will add a new user to the user.txt file
        - You can use the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same
            - If they are the same, add them to the user.txt file,
              otherwise present a relevant message'''
        
        # Only the admin is allowed to register users.
        if signed_on_user != 'admin':
            print("Only 'admin' can register users!")
            print()
        else:
            if signed_on_user == 'admin':        
                def register_user():
                    contents = '' 
                    with open("user.txt","r") as f:
                        contents = f.readlines()
    
                    usernames = []
                    passwords = []
    
                    for items in contents:
                        item1, item2 = items.split(", ")
                        usernames.append(item1)
                        passwords.append(item2)

                    user_credentials = dict(zip(usernames,passwords))
                    
                    # Learned about string punctuation from w3 schools.
                    # I did not know how to create a username that rejects special characters. 
                    special_characters = list(string.punctuation)
                        
                    print()
                    print("==== Username can only contain letters and numbers, no spaces ====")
                    print("==== Username should be between 5 and 15 characters ====")
                    username = input("Choose username: ").strip()
                    username = username.split()
                    username = "".join(username)
                    
                    # The username length should be between 5 and 15 characters.
                    if len(username) < 5 or len(username) > 15:
                        print("Username entered is less than 5 or greater that 15 characters.")    
                        register_user()

                    # Checks if the user already exists.
                    elif username in user_credentials:                            
                        print("Username already exists")
                        register_user()
                    
                    # Checks if the username contains alphanumeric characters(a-z) and (0-9) or underscores(_), if it doesn't, the register_user() function is called again.
                    elif username.isidentifier() == False:
                        print("Username can only contain letters and numbers")
                        register_user()
    
                    print()
                    print("==== Password length must be 8 to 25 characters ====")
                    print("==== Password should include atleast 1 uppercase letter, 1 numeral and a special character ====")
                    password = input("Choose password: ")
                    confirm_password = input("Confirm password: ")
        
                    if password != confirm_password:  
                        print("Password and confirmation do not match")
                        password = input("Choose password: ")
                        confirm_password = input("Confirm password: ")
                        register_user()
    
                    else:               
                        if len(password) < 8 or len(password) > 25:
                            print("Check your password length")
                            register_user()

                        # Learned how to use the any() function from w3schools.
                        # I didn't know how to check if the password contains special characters.
                        elif not any(i in password for i in special_characters):
                            print("You should add a special character for creating a strong password")
                            register_user()

                        # If the password does not contain any digits, the regiser_user() is called again.
                        elif not any(char.isdigit() for char in password):
                            print("Password should have atleast 1 numeral")
                            register_user()

                        # If the password does not contain any upper letters, the regiser_user() is called again.
                        elif not any(char.isupper() for char in password):
                            print("Password should include atleast 1 uppercase letter")
                            register_user()    

                        else:
                            password == confirm_password       
                            with open("user.txt","a") as f:           
                                f.write(f"{username}, {password}\n")
                                print("User registered successfully")
                                print()                
                register_user()

    elif menu == 'a':
        
        '''This code block will allow a user to add a new task to task.txt file
        - You can use these steps:
            - Prompt a user for the following: 
                - the username of the person whom the task is assigned to,
                - the title of the task,
                - the description of the task, and 
                - the due date of the task.
            - Then, get the current date.
            - Add the data to the file task.txt
            - Remember to include 'No' to indicate that the task is not complete.'''

        
        def add_task():
            username = input("Enter the username of the person to whom the task is assigned: ")
            contents = ""
            with open("user.txt", "r")as f:
                contents = f.readlines()
                
            usernames = []
            passwords = []
    
            for items in contents:
                item1, item2 = items.split(", ")
                usernames.append(item1)
                passwords.append(item2)

            user_credentials = dict(zip(usernames,passwords))
            # If the user tries to add a task before registering the user, the register user first message will be displayed.
            if username not in user_credentials:
                print("User not registered. Please register user first!")
                                
            else:
                # If the user does not enter the correct value for the inputs, the programme prompts the user to enter the values until all the entries are captured.
                task_title = input("Enter the title of the task: " )
                while len(task_title) < 1:                    
                    print("You didn't capture the task title!")
                    task_title = input("Enter the title of the task: " )
                
                task_description = input("Provide a description of the task: ")
                if len(task_description) < 1:    
                    print("You didn't capture the task description!")                    
                    task_description = input("Provide a description of the task: ")                    

                # Uses the current date for the task assigned date.                
                date_assigned = datetime.today()  
                
                date_due = input("Select the due date of the task; use this format. (yyyy-mm-dd): ")
                if len(date_due) < 10:    
                    print("You didn't capture the task due date correctly!")                    
                    date_due = input("Select the due date of the task: ")
                                        
                task_completed = "No"
                                                   
                with open("tasks.txt", "a") as f:
                    f.write(f"{username}, {task_title}, {task_description}, {date_assigned}, {date_due}, {task_completed}, \n")   
                    print("Task added successfully")
        add_task()        

    
    elif menu == 'va':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 in the PDF
            - It is much easier to read a file using a for loop.'''

        
        def view_all():                
            contents = ""
            with open("tasks.txt", "r") as f:
                contents = f.readlines()
    
            for lines in contents:
                lines = lines.split(", ")                    
                print(f"Task:\t\t\t{lines[1]}") 
                print(f"Assigned to:\t\t{lines[0]}")
                print(f"Date assigned:\t\t{lines[3]}")  
                print(f"Due date:\t\t{lines[4]}")  
                print(f"Task complete?:\t\t{lines[5]}")  
                print(f"Task description:\n{lines[2]}")
                print()
        
        view_all()
    
    
    elif menu == 'vm':
        pass
        '''This code block will read the task from task.txt file and
         print to the console in the format of Output 2 presented in the PDF
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the 
              username you have read from the file.
            - If they are the same you print the task in the format of Output 2
              shown in the PDF '''
        
        
        # Takes the signed on username as an argument to print the specific user's tasks.
        def view_mine():    
            username = signed_on_user             
            contents = ""
            with open("tasks.txt", "r") as f:
                contents = f.readlines()
    
            for lines in contents:
                lines = lines.split(", ")
                if lines[0] == username:
                    print(f"Task:\t\t\t{lines[1]}" ) 
                    print(f"Assigned to:\t\t{lines[0]}")
                    print(f"Date assigned:\t\t{lines[3]}")  
                    print(f"Due date:\t\t{lines[4]}")  
                    print(f"Task complete:\t\t{lines[5]}")  
                    print(f"Task description:\t{lines[2]}")
                    print()                        
        view_mine()

    
    elif menu == 'vs':                                                   
        # The function prints the total number of registered users.
        def registered_users():
            contents = "" 
            with open("user.txt","r") as f:
                contents = f.readlines()
    
            usernames = []
            passwords = []
                        
            for items in contents:
                item1, item2 = items.split(", ")
                usernames.append(item1)
                passwords.append(item2)                
            print("_______________Registered_users__________________")
            print()
                # I Learned about enumerate from w3 schools.
            # I did not know how to number items using a loop.
            for index, element in enumerate(usernames, 1):                
                print(f"{index}. {element}")

            print("_________________________________________________")
            print(f"Total registered users = {len(usernames)}")
            print("_________________________________________________")
            print()
        registered_users()
        
        
        # The function prints out the totals of assigned users and tasks.
        def totals():
            contents = ""
            with open("tasks.txt", "r") as f:
                contents = f.readlines()

            assigned_users = []
            tasks = []
            header1 = 'Assigned users'
            header2 = "Tasks"

            print("_________________________________________________")
            print(f"{header1.ljust(20)}|\t{header2}")    
            print("_________________________________________________")
            for items in contents:
                items = items.split(", ")        
                assigned_users.append(items[0])
                tasks.append(items[1])    
                print(f"{items[0].ljust(20)}| {items[1]}")

            total_users = len(assigned_users)
            total_tasks = len(tasks)
            print("_________________________________________________")
            print(f"Total users = {total_users}\t\tTotal tasks = {total_tasks}")
            print("_________________________________________________")
        totals()
            
           
    elif menu == 'e':
        print('Goodbye!!!')
        exit()
    
    else:
        print("You have entered an invalid input. Please try again")


