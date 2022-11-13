name = input("Enter your name : ").strip()
age = int(input('What\'s Your Age : ').strip())
print("="*100)
unit = input(' Please Choose Time Unit [\'months \'weeks \'days \'hours \'minutes \'second ] :'
             ' '.center(100, "#") + "\n").strip().lower()

months = age * 12
weeks = months * 4
days = weeks * 365
hours = days * 24
minutes = hours * 60
second = minutes * 60
# print(f"You lived is : {months} months , {weeks} weeks "
#       f", {days:,} days , {hours:,} hours , {minutes:,} and {second:,} second")


# update :  Calculate Age Advanced
if unit == "months" or unit == "m":
    print(f"you lived for {months:,} months ")
elif unit == "weeks" or unit == "w":
    print(f"you lived for {weeks:,} weeks ")
elif unit == "days" or unit == "d":
    print(f"you lived for {days:,} days ")
elif unit == "hours" or unit == "h":
    print(f"you lived for {hours:,} hours ")
elif unit == "minutes":
    print(f"you lived for {minutes:,} minutes ")
elif unit == "second":
    print(f"you lived for {minutes:,} second ")
else:
    print("Please , choose uni ")
