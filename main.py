import re
import urllib
import xlsxwriter

import xlrd


def register_user():
    regex_user_name = re.compile(r'([A-Za-z]{1,2}[A-Za-z0-9._%+-]+@[A-Za-z]+\.[A-Z|a-z]{2,})+')
    invalid_credentials = True
    username = ""
    password = ""
    while invalid_credentials:
        username = input("Enter user name:")
        if not re.fullmatch(regex_user_name, username):
            print("Invalid username !!! please enter again")
        else:
            password = input("Enter password:")
            if not (valid_password(password)):
                print("Invalid password !!! please enter again")
            else:
                invalid_credentials = False
    print("username:", username)
    print("password:", password)

    File_object = open(r"C:\\Users\\Akshay\\PycharmProjects\\RegisterAndLogin\\userCredentials.txt", "r+")
    File_object.write(username + " " + password)

    document_path = "C:\\Users\\Akshay\\PycharmProjects\\RegisterAndLogin\\userCredentials.xlsx"
    wb = xlsxwriter.Workbook(document_path)
    sh = wb.add_worksheet()
    sh.write_string(1, 1, username)
    sh.write_string(1, 2, password)


def valid_password(password):
    return_value = True
    special_characters = ['!', '@', '#', '$', '%', '&', '*']
    if len(password) < 5:
        print('Password length should be least of 5 characters')
        return_value = False

    if len(password) > 16:
        print('Password length should not be greater than 16')
        return_value = False

    if not any(char in special_characters for char in password):
        print('Password should have at least one special character(!@#$%&*)')
        return_value = False

    if not any(char.isdigit() for char in password):
        print('Password should have at least one number')
        return_value = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase character')
        return_value = False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase character')
        return_value = False

    return return_value


def login_user():
    username = input("Enter user name:")
    password = input("Enter password:")

    File_object = open(r"C:\\Users\\Akshay\\PycharmProjects\\RegisterAndLogin\\userCredentials.txt", "r+")
    credentails = File_object.readlines()
    credentialsArray = credentails[0].split(" ")
    saved_username = credentialsArray[0]
    saved_password = credentialsArray[1]

    if saved_username == username and saved_password == password:
        print("Logged in successfully")
    else:
        print("Failed to login please register")
        print("Press 1 for Registration")
        print("Press any other key for Forget Password")
        user_next_input = input("Enter your choise:")
        if user_next_input == '1':
            register_user()
        else:
            forget_user_password()


def forget_user_password():
    username = input("Enter user name:")
    File_object = open(r"C:\\Users\\Akshay\\PycharmProjects\\RegisterAndLogin\\userCredentials.txt", "r+")
    credentails = File_object.readlines()
    credentialsArray = credentails[0].split(" ")
    saved_username = credentialsArray[0]
    saved_password = credentialsArray[1]
    if saved_username == username:
        print("password is:", saved_password)
    else:
        print("Failed to retrieve password")
        print("Forwarding to user registration")
        register_user()


def main():
    user_main_input = 0
    while user_main_input != 4:
        print("Press 1 for Registration")
        print("Press 2 for Login")
        print("Press 3 for Forget Password")
        print("Press 4 to exit")
        user_main_input = input("Enter your choice:")
        if user_main_input == '1':
            register_user()
        if user_main_input == '2':
            login_user()
        if user_main_input == '3':
            forget_user_password()
        if not (user_main_input == '1' or user_main_input == '2' or user_main_input == '3' or user_main_input == '4'):
            print("Invalid input!!!")
            print("Please enter another choice from the lst")


if __name__ == '__main__':
    main()
