# created by : shehab shaat 20/8/2022

# ===============================assignment 1======================================
num1 = int(input("Enter number 1 : ").strip())
num2 = int(input("Enter number 2 : ").strip())
operation = input("Select Operation [+ , - , * , / , % ] : ").capitalize().strip()

result = ""
if operation == "+":
    # print(f"{num1} + {num2} = {num1+num2}")
    result = f"{num1} + {num2} = {num1 + num2}"

elif operation == "-":
    # print(f"{num1} - {num2} = {num1 - num2}")
    result = f"{num1} - {num2} = {num1 - num2}"

elif operation == "*":
    # print(f"{num1} * {num2} = {num1 * num2}")
    result = f"{num1} * {num2} = {num1 * num2}"

elif operation == "/":
    # print(f"{num1} / {num2} = {num1 / num2}")
    result = f"{num1} / {num2} = {num1 / num2}"
else:
    # print(f"{num1} % {num2} = {num1 % num2}")
    result = f"{num1} % {num2} = {num1 % num2}"

print(result)
print("=" * 50)
# # ===============================assignment 2======================================

age = 17
var = "App Is Suitable For You" if age > 16 else "App Is Not Suitable For You"
print(var)
print("=" * 50)

# ===============================assignment 3======================================
age = int(input("Enter your age :").strip())
months = 12 * age
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
chooseList = [1, 2, 3, 4, 5, 6]
if 10 < age < 100:
    units = input(
        '1-months\n2-weeks\n3-days\n4-hours\n5-minutes\n6-second\nPlease Choose Number Time Unit : \n').strip().lower()
    if units in chooseList:
        if units == "1":
            result = f"you lived for {months:,} months"
        elif units == "2":
            result = f"you lived for {weeks:,} weeks"
        elif units == "3":
            result = f"you lived for {days:,} days"
        elif units == "4":
            result = f"you lived for {hours:,} hours"
        elif units == "5":
            result = f"you lived for {minutes:,} minutes"
        else:
            result = f"you lived for {seconds:,} seconds"
            print(result)

    print("error !! , please enter number from 1 to 6")

else:
    print("age out of Range !!")

# ===============================assignment 4======================================
print("=" * 50)

countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
country = input("Input Your Country : ").capitalize().strip()
price = 100
discount = 30

if country in countries:
    result = f"Your Country Eligible For Discount And The Price After Discount Is ${price - discount}"
else:
    result = f"Your Country Not Eligible For Discount And The Price Is ${price}"

print(result)
