
name = input("Enter your name : ").strip
age = int(input('What\'s Your Age : ').strip())

months = age * 12 
weeks = months * 4 
days = weeks * 365
hours = days * 24
minutes = hours * 60
second = minutes * 60
print(f"You lived is : {months} months , {weeks} weeks , {days:,} days , {hours:,} hours , {minutes:,} and {second:,} second" )