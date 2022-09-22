# in
# not in
# name = "shehab"
# print("s" in name)
# print("r" in name)
#
# print("=" * 50)
# myList = ["Shehab", "Essam", "shat"]
# print("Shehab" in myList)
# print("Esam" not in myList)
# print("Esam" in myList)

arCountry = ["Palestine", "KSA", "Egypt", "Kuwait", "Jordan"]
enCountry = ["Usa", "italic"]
arDiscount = 80
enDiscount = 20
name = input("Enter Your name : ").strip().capitalize()
uCountry = input("Enter Your Country : ").strip().capitalize()
if uCountry in arCountry:
    print(f"hello {name} , you have a discount {arDiscount}")
elif uCountry in enCountry:
    print(f"hello {name} , you have a discount ${enDiscount}")
else:
    print("You have no discount")
