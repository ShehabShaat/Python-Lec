first_name = input('what\'s is your first name ?')
middle_name = input('what\'s is your middle name ?')
last_name = input('what\'s is your middle name ?')

print(first_name.strip() +" "+middle_name.strip()+" "+last_name.strip())
print(f"Hello {first_name.strip().capitalize()} {middle_name.strip().capitalize()} {last_name.strip().capitalize()} happy to see you .")
print(f"Hello {first_name.strip().capitalize()} {middle_name.strip().capitalize():.1s} {last_name.strip().capitalize()} happy to see you .")
