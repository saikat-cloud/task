


# def login(users):

#     while True:
#         username = str(input("please enter your user name: "))
#         password = str(input("please enter your password: "))

#         for user in users:
#             if username == user [0]:
#                 if password == user[1]:
#                     return username
                
#         print("Username or password is incorrect. Please try again!")


# users = [["saikat","s1234"],["riyad","r1234"]]
# username = login(users)

# print(username, "has loged in")




users = {}
status = ""

def login():
    status= input ("Are you registered user? y/n? Press q to quit: ")
    if status == "y":
        oldUser()
    elif status == "n":
        newUser()
    elif status == 'q':
        logout()


def newUser():
    name = input ("Create login name: ")

    if name in users:
        print("Login name already exist!")

    else:
        passwd = input ("Create password: ")
        users [name] = passwd
        print("User created")
        print(users)    #to see registerd users

def oldUser():
    oldname = input("Enter login name: ") 
    oldpasswd= input ("Enter password: ")

    if oldname in users and users [oldname] == oldpasswd:
        print("Login successful!")

    else:
        print("User doesn't exist or wrong password!")

def logout():
    exit()

while status != "q":
    login()


