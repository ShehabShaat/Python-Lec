# -------------------------------------------------------------------
# -- Object Oriented Programming => Class Methods & Static Methods --
# -------------------------------------------------------------------
# Class Methods:
# - Marked With @classmethod Decorator To Flag It As Class Method
# - It Takes Cls Parameter Not Self To Point To The Class not The Instance
# - It Doesn't Require Creation of a Class Instance
# - Used When You Want To Do Something With The Class Itself
#  نستخدمها لاي حالة من الحالات المحتاجة للتعامل مع الكلاس  وليس الانستانس
# -----------------------------------------------------------

class Member:
    not_allowed_name = ['shehab', 'essam', 'shaat']
    user_num = 0

    @classmethod
    def show_user_count(cls):
        print(f"We Have {cls.user_num} Users In Our System")

    def __init__(self, f_name, m_name, l_name, gender):
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        self.gender = gender
        Member.user_num += 1

    def full_name(self):
        if self.f_name in Member.not_allowed_name:
            raise ValueError(" Name Not Allowed!!")
        else:
            return f"{self.f_name} {self.m_name} {self.l_name}"

    def say_hello(self):
        if self.gender == "male":
            return f"Hello Mr {self.f_name} "
        else:
            return f"Hello Miss {self.f_name} "

    def full_info(self):
        # return f"{Member.say_hello(self)} and your full name {Member.full_name(self)}"
        return f"{self.say_hello()} and your full name {self.full_name()}"

    def delete_user(self):
        Member.user_num -= 1
        return f"User {self.f_name} deleted !!"


member_one = Member("sheHab", "essam", "shaat", "male")
member_two = Member("abOod", "essam", "shaat", "male")
member_three = Member("nour", "essam", "shaat", "female")
print(member_one.full_name())
print(member_one.say_hello())
print(member_one.full_info())
print(Member.user_num)
print(member_one.delete_user())
print(Member.user_num)
Member.show_user_count()
#
# print(Member.full_name(member_one))
# print(member_one.full_name())
# ==================================================================================
# Static Methods:
# - It Takes No Parameters
# - Its Bound To The Class Not Instance
# - Used When Doing Something Doesnt Have Access To Object Or Class But Related To Class