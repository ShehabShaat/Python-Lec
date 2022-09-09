from datetime import datetime

print(datetime.now())
# print current year only
print(datetime.now().year)

# print current month only
print(datetime.now().month)

# print current day only
print(datetime.now().day)

# print currint time
print(datetime.now().time())
print(datetime.now().time().hour)
print(datetime.now().time().minute)
print(datetime.now().time().second)
print(datetime.now().time().microsecond)

# print start and end  of date بداية ونهاية التاريخ
print(datetime.max)
print(datetime.min)

# print start and end  of date بداية ونهاية الوقت
import datetime

print(datetime.time.min)
print(datetime.time.max)
# print specific time
print(datetime.datetime(2000, 8, 5))
print(datetime.datetime(2000, 8, 5, 10, 20))

#
print("=" * 50)
myBirthDay = datetime.datetime(2000, 8, 5)
date_now = datetime.datetime.now()
lived = date_now - myBirthDay
print(f"my birth day is {myBirthDay} and ", end="")
print(f"the date now is  {date_now}")
print(f"i lived {lived.days} days")
print(f"i lived {lived} ")
# ======================strftime=============================
# review https://strftime.org/
print(myBirthDay.date())
print(myBirthDay.strftime("%d"), end=" ")
print(myBirthDay.strftime("%B"), end=" ")
print(myBirthDay.strftime("%Y"))
# or
print(myBirthDay.strftime("%d %B %Y"))
print(myBirthDay.strftime("%d %B %y"))

myDateList = []
while len(myDateList) < 3:
    myDateList.extend(map(int, input().split()))

mm = myDateList[0]
dd = myDateList[1]
yy = myDateList[2]
yourBirthDay = datetime.datetime(yy, mm, dd)
print(yourBirthDay.strftime("%A").upper())
