
# if , elif , else , nested if and Trainigs

Uname = input("Enter Your Name : ").capitalize().strip()
country = input("Enter Your Country : ").capitalize().strip()
isStudent = input("are you student ?").strip().lower()
cName = "Python"
cPrice = 100
cDiscount = 50

if country == "Palestine" or country == "Egypt":
    
    if isStudent =="yes" : 
       print(f"Hello {Uname} Because You Are From {country} And Student")
       print(f"The Course \" {cName}\" Prise Is: ${cPrice-90}")
    else :
        print(f"Hello {Uname} Because You Are from {country}")
        print(f"The Course \" {cName}\" Prise Is: ${cPrice-80}")
    
elif country == "USA" : 
    print(f"Hello {Uname} Because You Are from {country}")
    print(f"The Course \" {cName}\" Prise Is: ${cPrice-30}")
    
else : 
    print(f"Hello {Uname} Because You Are from {country}")
    print(f"The Course \" {cName}\" Prise Is: ${cPrice-cDiscount}")
    print("="*100)
    
    
    # ==================================================================================
    # ernary Conditional Operator
    print("="*50)
    wCountry = input("Enter Your Country : ").capitalize().strip()
    if wCountry == "Palestine" : print(f"The wether in {wCountry} is 15")
    elif wCountry == "KSA" : print(f"The wether in {wCountry} is 50")
    else : print(f"The wether in {wCountry} is 10")
    

movieRate = 18
age = 16
if age > movieRate: print("movie is good for you")
else : print("movie is not good for you")
        # sort if 
print("movie is good for you" if age > movieRate else "movie is not good for you")