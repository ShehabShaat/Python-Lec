# created by : shehab shaat 11/9/2022

# ===============================assignment 1======================================
import datetime

Today = datetime.datetime.now()
your_date = datetime.datetime(2022, 7, 27)
print(f"Days From {your_date.date()} To {Today.date()} Is => {(Today - your_date).days}")

# ===============================assignment 2======================================

print(Today.date())
print(Today.strftime("%b %d, %Y"))
print(Today.strftime("%d - %b - %Y"))
print(Today.strftime("%d / %b / %y"))
print(Today.strftime("%d / %B / %Y"))
print(Today.strftime("%a, %d %B %Y"))
