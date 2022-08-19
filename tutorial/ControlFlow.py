


Uname = input("Enter Your Name : ").capitalize().strip()
country = input("Enter Your Country : ").capitalize().strip()
cName = "Python"
cPrice = 100
cDiscount = 50

if country == "Palestine" or country == "Egypt":
    print(f"Hello {Uname} Because You Are from {country}")
    print(f"The Course \" {cName}\" Prise Is: ${cPrice-80}")
    
elif country == "USA" : 
    print(f"Hello {Uname} Because You Are from {country}")
    print(f"The Course \" {cName}\" Prise Is: ${cPrice-30}")
    
else : 
    print(f"Hello {Uname} Because You Are from {country}")
    print(f"The Course \" {cName}\" Prise Is: ${cPrice-cDiscount}")
    
    