
# created by : shehab shaat 18/8/2022

# ===============================assignment 1=====================================

# True value
print(bool(5>4))
print(5>3)
print(bool("5>3"))
print(bool(True))
print(bool(" "))

# False value
print(bool(5<4))
print(5<3)
print(bool(False))
print(bool(""))
print(bool(None))

# ===============================assignment 2======================================

Python = 80
Kotlin = 60
java = 70
print("="*50)

print(Python>50 and Kotlin>50  and java>50 )
# print((Python and Kotlin and java )>50) ather solve
print("="*50)

# ===============================assignment 3======================================
num_one = 10
num_two = 20
num = 20

print(num > num_one or num > num_two)
print(num > num_one and num > num_two)
print("="*50)

# ===============================assignment 4======================================
num_one = 10
num_two = 20
resultSum = num_one + num_two
resultExp = resultSum**3
resultMod =resultExp % 26000
resultdiv =resultMod/ 5
print(resultSum)
print(resultExp)
print(resultMod)
print(resultdiv)
# print(type(resultdiv))
print(type(str(resultdiv)))
print("="*50)

# ===============================assignment 5======================================


name = input("Enter your name : ").strip().capitalize()
print(f"Hello {name} , Happy To See You Here.")
print("="*50)

# ===============================assignment 6======================================
age = int(input("Enter your age : "))

if age >= 16 :
  print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")
else :
  print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
  
# ===============================assignment 7======================================
  
  
First_Name = input("Enter your name : ").strip().capitalize()

Second_Name = input("Enter your middile name : ").strip().capitalize()

print(f"Hello {First_Name} {Second_Name:.1s}")
print("="*50)

# ===============================assignment 8======================================

email = input("Enter Your Email : ").strip().lower()
print("Your Name Is "+email[:email.index("@")].capitalize())
print("Email Service Provider Is "+email[email.index("@")+1:email.index(".")])
print("Top Level Domain Is "+email[email.index(".")+1:])
