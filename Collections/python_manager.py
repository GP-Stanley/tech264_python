"""Create a program that is a mini password manager
You will practice using dictionaries

First, setup the ability for one user to login to the account manager using a username + password

Once logged in, they should be able to store a usernames and passwords for different
accounts so they don't need to remember all their passwords
For example, for Facebook, email account, etc

Once the storage is setup, add the ability to add new users to the account manager
(they will each need a username + password)

Add the ability to retrieve the username and password for a specific account if they input the account name e.g. hotmail

If time - Can you make it so you need to enter the user's password before they can change it to something else?
"""

"""Set-up user login"""

users = {"admin": "password123"}                            # Dict to store user credentials

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    if username in users and users[username] == password:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

if not login():                                         # Login the user
    exit()


"""Store Usernames and Passwords for various accounts"""

accounts = {}                       # Dict to store account information.

def add_account():
    account_name = input("Enter the account name (e.g., Facebook): ")
    account_username = input("Enter the account username: ")
    account_password = input("Enter the account password: ")
    accounts[account_name] = {"username": account_username, "password": account_password}
    print(f"Account {account_name} added successfully!")

def view_account():
    account_name = input("Enter the account name to retrieve: ")
    if account_name in accounts:
        print(f"Username: {accounts[account_name]['username']}")
        print(f"Password: {accounts[account_name]['password']}")
    else:
        print("Account not found.")

add_account()                                   # add and view accounts.
view_account()


"""Add new users (to the account manager)"""

def add_user():
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    if new_username in users:
        print("Username already exists.")
    else:
        users[new_username] = new_password
        print(f"User {new_username} added successfully!")


add_user()                                                      # Add a new user


"""Retrieve username and password for a specific account"""
# this is in the view_account function.

"""Change password with verification"""

def change_password():
    account_name = input("Enter the account name to change the password: ")
    if account_name in accounts:
        current_password = input("Enter the current password: ")
        if accounts[account_name]["password"] == current_password:
            new_password = input("Enter the new password: ")
            accounts[account_name]["password"] = new_password
            print(f"Password for {account_name} changed successfully!")
        else:
            print("Incorrect current password.")
    else:
        print("Account not found.")


change_password()                                       # Change account password







