
# email = "shaatshehab@gmail.com"
# print(email[:email.index("@")])


name = input("Enter Your Name : ").strip().capitalize()
email = input("Enter Your Email : ").strip()

username = email[:email.index("@")]
website = email[email.index("@")+1:]
print(f"Hello {name} , Your Email Is {email}\nThe Username Is : {username} And Your Website Is : {website}")