admins = ["Sh.shat", "Ahmed", "Ali", "Osama", "Mohammed"]
username = input("Enter username admin : ").strip().capitalize()
if username in admins:
    print(f"Hello {username}, Wellcome Back")
    option = input("delete or update : ").strip().lower()
    if option == "update":
        newname = input("Enter new username pleas : ")
        admins[admins.index(username)] = newname
        print("the username is updated..")
        # print(admins)
    elif option == "delete":
        admins.remove(username)
        print("the username is deleted..")
        # print(admins)
    else:
        print("Wrong option chose..")

else:
    print("your not admin, add u ? Y or N ")
    ans = input("Enter Your Answer : ").strip().capitalize()
    if ans == "Y" or "yes":
        admins.append(username)
        print("your name is added..")
        # print(admins)
    else:
        print("u are not added ")
