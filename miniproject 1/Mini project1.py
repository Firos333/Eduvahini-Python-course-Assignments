import os
import datetime
def userauthentocation():

    print("Press 1 for Login ")
    print("      2 for Create account")
    print("      3 for Exit \n")

    x = input()
    return x

def login(username,password):
    userdetails = open("user.txt", 'r')
    users = userdetails.readlines()
    for user in users:
        user_information = user.split()
        if user_information[0]== username and user_information[1]== password:
           return True
        else:
            pass






def diary(username):
    exit=True
    while exit:
        print("Enter 1 to read your Diary")
        print("      2 to make an entry to the diary for today")
        print("      3 to go Back\n")
        choice = input()
        if choice=="1":
            print("----------------------------------------------------")
            print("                     Your diary                     ")
            print("----------------------------------------------------")
            cwd=os.getcwd()
            folder = os.path.join(cwd, username)
            path=cwd+"/"+username
            try:
                files=os.listdir(path)
                print(files)
                if files:
                    diary_found = True
                    while diary_found: #checking given date is correct or not
                        for file in files:
                                print(file)
                        print("\n")
                        print("enter the date of diary which you want to read (must include .txt extension along with date")
                        date = input()
                        cwd=os.getcwd()
                        if date in files:  # checking dairy found in given date or not
                            folder = os.path.join(cwd, username)
                            file = os.path.join(folder, date)
                            diary = open(file, 'r')
                            print("***************************************")
                            print(diary.read())
                            print("***************************************")

                            diary_found = False
                        else:
                            diary_found = True
                            print("you are selcted a wrong date\n")

                    #exit=False
                else:
                    print("there is no diary")
                    exit=True
            except OSError:
                print("You dont have any diary entry yet")
            else:
                pass


        elif choice=="2":
            print("----------------------------------------------------")
            print("              Write your today diary                ")
            print("----------------------------------------------------")
            date=datetime.date.today()
            file_name =date.strftime("%d-%b-%Y")
            print("Write your diary here..\n")
            cwd=os.getcwd()
            path=cwd+"/"+username
            try:
                os.mkdir(path)
                while True:
                    file = os.path.join(path, file_name)
                    diary = open(file + '.txt', 'a')
                    entity=input()
                    if entity=="":
                        entity = input()
                        if entity=="":
                            entity = input()
                            if entity == "":
                                break
                    else:
                        diary.write(entity)
                        diary.write('\n')
                        exit = False

            except OSError:
                print("You are already enterd today diary")
            else:
                print("*********************************")
                print("your diary saved succesfully ")
        elif choice == "3":
            break
        else:
            print("wrong choice")



#for creating new account
def signup():
    print("----------------------------------------------------")
    print("                   signup                    ")
    print("----------------------------------------------------")
    username = input("Enter Your Username:\n")
    password = input('Enter Password:\n')
    try:
        userdetails = open("user.txt", 'r')
    except:
        userdetails = open("user.txt", 'w')
        userdetails.close()
        userdetails = open("user.txt", 'r')
    else:
        print("usercreation failed")

    details=userdetails.read()
    if (username in details):
        print("alreaady exist")
        username_exist =True
        while username_exist:
            print("The username already exist")
            username = input('Enter another username')
            if (username in details):
                username_exist = True
            else:
                password = input('Enter Password')
                return username,password
                username_exist = False

    else:

        return username,password

def logout():
    print("----------------------------------------------------")
    print('                   Thank you                         ')
    print("----------------------------------------------------")

    Q=input("press 'q' to exit \n")
    if Q=='q':
        print("")


#main program..

print("----------------------------------------------------")
print("                 User Diary system                  ")
print("----------------------------------------------------")
usernew=False
while usernew==False:
    x = userauthentocation()
    if x=='1':
        print("----------------------------------------------------")
        print("                     LOGIN HERE                     ")
        print("----------------------------------------------------")
        username = input("Enter Username:\n")
        password = input('Enter Password:\n')
        if login(username,password):
            print("----------------------------------------------------")
            print("              You are login successfully            ")
            print("----------------------------------------------------")
            print('       Welcome '+username    )
            print("    ***********************    ")
            diary(username)
            print("\n")
            print("\n")
            usernew = True
        else:

            print("----------------------------------------------------")
            print("Incorrect username or password")
            usernew=False
    elif x=='2':
        username,password=signup()
        user = open("user.txt", 'a')
        user.write(username)
        user.write(" ")
        user.write(password)
        user.write("\n")
        user.close()
        print("\n")
        diary(username)
        print("\n")

        usernew = True
    elif x=='3':
        usernew=True
    else:
        print("invalid choice")


    print("----------------------------------------------------")
    print('                   Thank you                         ')
    print("----------------------------------------------------")

    #Q = input("press any key to exit \n")
    if input("press any key to exit \n") :
        print("")
        break