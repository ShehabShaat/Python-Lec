mySkills = {
    "Python": "70%",
    "Kotlin": "90%",
    "Java": "80%",
    "C++": "90%"

}
myTuple = ("Kotlin", "java", "C++")


def Skill1(name, *skill, **skills):
    print(f"hello {name}\nyour skills is : ")
    for Skills in skill:
        print(f"- {Skills}")
    print(f"your skills is and Progress : ")
    for k, v in skills.items():
        print(f"{k} => {v} ")


Skill1("Shehab", *myTuple, **mySkills)
print("="*50)
Skill1("Shehab", "Kotlin", "java", "C++", **mySkills)
print("="*50)

Skill1("Shehab", "Kotlin", "java", "C++", python="80%", Java="90%", C="100%", Kotlin="80%")
print("="*50)
Skill1("Shehab")
