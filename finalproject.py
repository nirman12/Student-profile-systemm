#Batsal:
class Admin:
    def __init__(self, user_file, password_file):
        self.user_file = user_file
        self.password_file = password_file
        self.user_data = []
        self.password_data = []
        self.index = []

    def userf_load(self):
        try:
            file = open(self.user_file, 'r')
            self.user_data = file.readlines()
        except FileNotFoundError:
            print("(The user file is not found)")

    def password_load(self):
        try:
            file = open(self.password_file, 'r') 
            self.password_data = file.readlines()
        except FileNotFoundError:
            print("(The password file is not found)")

    def user_save(self):
        file = open(self.user_file, 'w')
        file.writelines(self.user_data)

    def pass_save(self):
        file = open(self.password_file, 'w')
        file.writelines(self.password_data)

    def register_student(self, username, password):

        self.user_data.append(username + '\n')
        self.password_data.append(password + '\n')
        self.user_save()
        self.pass_save()

    def remove_student(self, username):
        try:
            self.index = self.user_data.index(username + '\n')
            del self.user_data[self.index]
            del self.password_data[self.index]
            print(f"(User '{username}' removed successfully.)")
        except ValueError:
            print(f"(User '{username}' not found.)")

        self.user_save()
        self.pass_save()

    def modify_student(self, username):
        try:
            self.index = self.user_data.index(username + '\n')
            new_username = input('Enter the new username: ')
            new_password = input('Enter the new password: ')
            self.user_data[self.index] = new_username + '\n'
            self.password_data[self.index] = new_password + '\n'
            print(f"(User '{username}' modified successfully.)\n")
        except ValueError:
            print(f"(User '{username}' not found.)")

        self.user_save()
        self.pass_save()
#Nirman
    def view_users(self):
        try:
            i = 0
            print("\nThe users are:")
            for user in self.user_data:
                i +=1
                print(f"{i}.{user[:-1]}")  # Removes newline character from each line
        except  IndexError:
            print("(No users available.)")

    def user_verification(self, username, password):
        try:
            index = self.user_data.index(username + '\n')
            if self.user_data[index] == username+'\n' and self.password_data[index] == password+'\n':
                return True
            else:
                print('\n(Incorrect username or password...)')
                return False  # Return False if the username or password is incorrect
        except ValueError:
            print(f"\n(User '{username}' not registered.)")
            return False  # Return False if the username is not found

#Prakrist:
class User(Admin):
    def __init__(self,grade_file,eca_file):
        self.grade_file=grade_file
        self.eca_file=eca_file
        self.grade_data=[]
        self.eca_data=''
        self.subjects = ['English','math','IT','FOD','FOM']

    def grades_upload(self):
        try:
            file = open(self.grade_file, 'r')
            self.grade_data = file.readlines()
        except FileNotFoundError:
            print("\n(The grade file is not found. Might need to update your profisle first.)")

    def eca_upload(self):
        try:
            file = open(self.eca_file, 'r')
            self.eca_data = file.readlines()
        except FileNotFoundError:
            print("\n(The ECA file is not found. Might need to update your profile first.)")

    def store_grades(self):
        file = open(self.grade_file, 'w') 
        file.writelines(self.grade_data)

    def store_eca(self):
        file = open(self.eca_file, 'w') 
        file.writelines(self.eca_data)

    def view_grades(self):
        try:
            n = 0
            print("\nYour grades are:\n")
            for i in range(len(self.subjects)):
                n  = i + 1
                print(f"{n}.{self.subjects[i]}: {self.grade_data[i]}")

        except  FileNotFoundError:
            print('\n(No grades information available\nPlease add your grades first.)')

    def view_eca(self):
        try:
            print("\nECA details:")
            if not self.eca_data:
                print('None')
            else:
                print(f"Currently engaged in \"{(''.join(self.eca_data))}\"")  # Removes newline character from each line
        except  FileNotFoundError:
            print('\n(No ECA information available\nPlease add your ECA engagement first.)')
#Nirman
    def grades_modification(self):
        try:
            print(self.subjects)
            for subject in self.subjects:
                index = self.subjects.index(subject)
                new_mark=input(f'Enter the updated marks for {subject}: ')
                self.grade_data[index] = new_mark + '\n'
            print("(Modified successfully.)\n")
        except IndexError:
            print("(Marks not found.)")
            add_grades = input('Would you like to add your grades? (y/n) ').lower()
            if add_grades == 'y':
                for subject in self.subjects:
                    grade = input(f'Enter your grade for {subject}: ')
                    self.grade_data.append(grade + '\n')
            else:
                return False
        except FileNotFoundError:
            print("Error: Grade file not found.")
            return False
        
        self.store_grades()
        return True
    
    def eca_modification(self):
        try:
            self.eca_data = input('\nWhat activity are you currently engaged with? ')
            self.store_eca()
            print("(Updated Successfully.)\n")
        except IndexError:
            print("(ECA activity not found.)")
            add_E = input('\nWoulld you like to add you Eca details? (y/n) ').lower()
            if add_E == 'y':
                    eca = input('What activity are you currently engaged with? (write): ')
                    self.eca_data.append(eca + '\n')
            else:
                return False
        except FileNotFoundError:
            print("Error: Eca file not found.")
        self.store_eca()

#Utiraj
TheAdmin = Admin('users.txt', 'passwords.txt')
TheAdmin.userf_load()
TheAdmin.password_load()

while True:
    print('\n\n\t\t__Student Profile Systen\n\n')
    choice1 = input("\t[1]Admin\t[2]User\t\t[3]Exit\n\nEnter the selection number: ")
    if choice1 == "1":
        while True:
            admin_choice = input("\n[1]Register student profile\n[2]Modify student's username and password \n[3]Remove student profile\n[4]Go back\n\n Select option: ")
            if admin_choice == "1":  
                username = input('Create username: ')
                passwrd = input('Create password: ')
                TheAdmin.register_student(username, passwrd)
            elif admin_choice == "2":  
                modipy = input('Enter the user to modify: ')
                TheAdmin.modify_student(modipy)
                
            elif admin_choice == "3":
                TheAdmin.view_users()
                action = input('Enter the username to remove the user: ')
                TheAdmin.remove_student(action)
                
            elif admin_choice == "4":
                break
            else:
                print('Invalid Option')
                
    elif choice1 == "2":   # User Login 
        name = input('Enter your username: ')
        password = input('Enter your password: ')
        value = TheAdmin.user_verification(name,password)

        if value:
            TheUser = User('grades.txt','eca.txt')
            TheUser.grades_upload()
            TheUser.eca_upload()

            while True:
                user_choice = input('\n[1]View your grades \n[2]View your Eca details\n[3]Update your profile\n[4]Go back\n\nSelect option: ')
                if user_choice == '1':
                    TheUser.view_grades()
                elif user_choice == '2':
                    TheUser.view_eca()
                elif user_choice == '3':
                    eg = input('\n[1]Grades\t[2]Eca\n[3]Go back\n\nSelect option to update: ')
                    if eg == '1':
                        TheUser.grades_modification()
                    elif eg == '2':
                        TheUser.eca_modification()
                    elif eg  == '3':
                        break
                    else:
                        print("Invalid Option")
                elif user_choice == '4':
                    break
                else:
                    print("Invalid Option")

        else:
            print("\nUsername or Password is incorrect.\nPlease try again.")

    else:
        print('Exiting program')
    break
