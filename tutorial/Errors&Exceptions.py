# num = "10"
# if type(num) != int:
#     raise Exception("Only number Allowed")  # exception
#     # or
#     # raise ValueError("Only number Allowed")  # exception
#
# print("msg after if condition")

# =============================================================================================
# Try Except , Else ,Finally
# try:
#     num = int(input("Enter Your Number :"))
#
# except:
#     print("this is not integer")
#
# else:
#     print(num)
# finally:
#     print("print finally what ever happened")

try:
    # print(x)
    # print(10 / 0)
    print(int("input"))
except NameError:
    print("x is undefined")
except ZeroDivisionError:
    print("can not divide")
except ValueError:
    print("Value Error")
