# ----------------------------------------------------------
# -- Object Oriented Programming => Class Syntax and Info --
# ----------------------------------------------------------
# [01] Class is The Blueprint(مخطط) Or Constructor Of The Object
# [02] Class Instantiate Means Create Instance( الاوبجكت الي بتنشأه من الكلاس)of A Class
# [03] Instance => Object Created From Class And Have Their Methods and Attributes
# [04] Class Defined With Keyword class
# [05] Class Name Written With PascalCase [UpperCamelCase] Style
# [06] Class May Contains Methods and Attributes
# [07] When Creating Object Python Look For The Built In __init__ Method
# [08] __init__ Method Called Every Time You Create Object From Class
# [09] __init__ Method Is Initialize The Data For The Object
# [10] Any Method With Two Underscore in The Start and End Called "Dunder" or Magic Method
# [11] self Refer To The Current Instance Created From The Class And Must Be First Param
# [12] self Can Be Named Anything
# [13] In Python You Dont Need To Call new() Keyword To Create Object
# ==============================================================================
# -- Object Oriented Programming => Instance Attributes and Methods --
# --------------------------------------------------------------------
# Self: Point To Instance Created From Class
# Instance Attributes: Instance Attributes Defined Inside The Constructor
# -----------------------------------------------------------------------
# Instance Methods: Take Self Parameter Which Point To Instance Created From Class
# Instance Methods Can Have More Than One Parameter Like Any Function
# Instance Methods Can Freely Access Attributes And Methods On The Same Object
# Instance Methods Can Access The Class Itself
# -----------------------------------------------------------
class Member:
    def __init__(self, f_name, m_name, l_name, gender):
        self.f_name = f_name
        self.m_name = m_name
        self.l_name = l_name
        self.gender = gender

    def full_name(self):
        return f"{self.f_name} {self.m_name} {self.l_name}"

    def say_hello(self):
        if self.gender == "male":
            return f"Hello Mr {self.f_name} "
        else:
            return f"Hello Miss {self.f_name} "

    def full_info(self):
        # return f"{Member.say_hello(self)} and your full name {Member.full_name(self)}"
        return f"{self.say_hello()} and your full name {self.full_name()}"


member_one = Member("shehab", "essam", "shaat", "male")
print(member_one.full_name())
print(member_one.say_hello())
print(member_one.full_info())
