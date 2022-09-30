# created by : shehab shaat 30/9/2022

# ===============================assignment 1======================================

class Game:
    def __init__(self, name, developer, year, price):
        self.name = name
        self.developer = developer
        self.year = year
        self.price = price * 15.6

    def price_in_pounds(self):
        return self.price


game_one = Game("Ys", "Falcon", 2010, 50)

print(f"Game Name Is \"{game_one.name}\", ", end="")
print(f"Developer Is \"{game_one.developer}\", ", end="")
print(f"Release Date Is \"{game_one.year}\", ", end="")
print(f"Price In Egypt Is {game_one.price_in_pounds()} Egyptian Pounds", end="")
print()

print("=" * 50)


# Needed Output
# "Game Name Is "Ys", Developer Is "Falcon", Release Date Is "2010", Price In Egypt Is 780.0 Egyptian Pounds"

# ===============================assignment 2======================================
class User:
    def __init__(self, f_name, l_name, age, gender):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender

    def full_details(self):
        if self.gender == "male":
            return f"Hello Mr {self.f_name} {self.l_name[0]}. {40 - self.age} Years To Reach 40"
        else:
            return f"Hello Mrs {self.f_name} {self.l_name[0]}. [{40 - self.age}] Years To Reach 40"


user_one = User("Osama", "Mohamed", 38, "Male")
user_two = User("Eman", "Omar", 25, "Female")

print(user_one.full_details())  # Hello Mr Osama M. [02] Years To Reach 40
print(user_two.full_details())  # Hello Mrs Eman O. [15] Years To Reach 40

print("=" * 50)


# ===============================assignment 3======================================

class Message:
    @classmethod
    def print_message(cls):
        return "Hello From Class Message"


# Write Class Content

print(Message.print_message())

print("=" * 50)


# Output
# Hello From Class Message

# ===============================assignment 4======================================
class Games:

    def __init__(self, string):
        self.string = string

    def show_games(self):
        if type(self.string) == str:
            print(f"I Have One Game Called \"{self.string}\" ")
        elif type(self.string) == list:
            print("I Have Many Games:")
            for _ in self.string:
                print(_)
        elif type(self.string) == int:
            print(f"I Have {self.string} Game")


my_game = Games("Shadow Of Mordor")
my_games_names = Games(["Ys II", "Ys Oath In Elhanan", "YS Origin"])
my_games_count = Games(80)

my_game.show_games()
# Output
# I Have One Game Called "Shadow Of Mordor"

my_games_names.show_games()

# Output
# I Have Many Games:
# -- Ys II
# -- Ys Oath In Elhanan
# -- YS Origin

my_games_count.show_games()
# Output
# I Have 80 Game.

print("=" * 50)


# ===============================assignment 5=============================================
# Main Class
class Members:

    def __init__(self, n, p):
        self.name = n

        self.permission = p

    def show_info(self):
        return f"Your Name Is {self.name} And You Are {self.permission}"


class Admins(Members):
    def __init__(self, n, p):
        super().__init__(n, p)


class Moderators(Admins):
    def __init__(self, n, p):
        super().__init__(n, p)


member_one = Admins("Osama", "Admin")
member_two = Moderators("Ahmed", "Moderator")

print(member_one.show_info())
# Output
# Your Name Is Osama And You Are Admin

print(member_two.show_info())

# Output
# Your Name Is Ahmed And You Are Moderator
print("=" * 50)


# ===============================assignment 6=============================================
class A:

    def __init__(self, one):
        self.one = one


class B:

    def __init__(self, two):
        self.two = two


class C:

    def __init__(self, three):
        self.three = three


class Text(A, B, C):
    def __init__(self, one, two, three):
        A.__init__(self, one)
        B.__init__(self, two)
        C.__init__(self, three)

    def show_name(self):
        return f"The Name Is {self.one}{self.two}{self.three}"


the_name = Text("El", "ze", "ro")

print(the_name.show_name())

# Output
# The Name Is Elzero
