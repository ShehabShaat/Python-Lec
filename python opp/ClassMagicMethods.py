# --------------------------------------------------
# -- Object Oriented Programming => Magic Methods --
# --------------------------------------------------
# Everything in Python is An Object
# __init__  Called Automatically When Instantiating Class
# self.__class__ The class to which a class instance belongs
# __str__   Gives a Human-Readable Output of the Object
# __len__   Returns the Length of the Container
#           Called When We Use the Built-in len() Function on the Object
# ------------------------------------------------------
class Skill:
    def __init__(self):
        self.skills = ["Html basics", "Css basics", "js basics", "Python", "Django"]

    def __str__(self):
        return f"this my skills : {self.skills}"

    def __len__(self):
        return len(self.skills)


profile = Skill()  # profile => instance
# print(profile.__class__)  # يعني هذه الانستانس تنتمي لاي كلاس
print(profile)
print(len(profile))
profile.skills.append("Data-Scientists")
print(profile)

print(len(profile))
