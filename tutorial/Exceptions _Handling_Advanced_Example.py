tries = 5
my_file = None
print("Enter your file name with abs path to open:")
print(r"Example :C:\Users\shehab\Desktop\PythonTutorial\tutorial\files\your_file.txt")
while tries > 0:
    print(f"You Have {tries} Tries Left")
    try:
        file_name_path = input("File Name : ").strip()
        my_file = open(file_name_path, "r")
        print(my_file.read())
        break

    except FileNotFoundError:
        print("file not found , try agine.. ")
        tries -= 1
    except:
        print("found Error , try agine..")
        tries -= 1
    finally:
        if my_file is not None:
            my_file.close()
            print("file closed")
else:
    print("All Tries Are Done")
