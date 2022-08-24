#  created by : shehab shaat 24/8/2022
# ===============================assignment 1======================================

def get_score(**name):
    for k, v in name.items():
        print(f"{k} => {v}")


get_score(Math=90, Science=80, Language=70)
print("=" * 50)
get_score(Logic=70, Problems=60)


# ===============================assignment 2======================================
def get_people_scores(*name, **skills):
    if len(name) == 0:
        for k, v in skills.items():
            print(f"{k} => {v}")
    elif len(skills) == 0:
        print(f"Hello {name} You Have No Scores To Show")
    else:
        print(f"Hello {name} This Is Your Score Table:")
        for k, v in skills.items():
            print(f"{k} => {v}")


get_people_scores("Osama", Math=90, Science=80, Language=70)
get_people_scores("Mahmoud", Logic=70, Problems=60)
get_people_scores(Logic=70, Problems=60)
get_people_scores("Ahmed")

