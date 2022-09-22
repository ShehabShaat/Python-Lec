tries = 5
yourPassword = "SheHab"
Password = input("Enter Your Password :")
while Password != yourPassword:
    tries -= 1
    print(f"Password is Wrong , Try again.. {'last'if tries ==0 else tries} chance Left")
    Password = input("Enter Your Password :")
    if tries == 0:
        print("All Tries IS finished")
        break
else:
    print("You are logged in successfully")
