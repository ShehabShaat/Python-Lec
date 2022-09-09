# # # n = int(input())  # Number of elements
# # # List = [int(elem) for elem in input().split(" ")]
# # # print(List)
# # # ==========================================================================
# # # enCourse = int(input())
# # # myList1 = list(map(int, input().split(" ")))
# # #
# # # frCourse = int(input())
# # # myList2 = list(map(int, input().split(" ")))
# # #
# # # myList1 = set(myList1)
# # # myList2 = set(myList2)
# # # count = 0
# # # for s in myList1.symmetric_difference(myList2):
# # #     count += 1
# #
# # # print(count)
# # # ===============================================================
# # #  leap day
# # # def is_leap(y):
# # #     if y % 4 == 0:
# # #         if y % 100 != 0:
# # #             return True
# # #         else:
# # #             if y % 400 == 0:
# # #                 return True
# # #             else:
# # #                 return False
# # #     else:
# # #         return False
# # #
# # #
# # # year = int(input())
# # # Output = bool(is_leap(year))
# # # print(Output)
# #
# # # =========================================================
#
# # List = []
# # N = int(input())
# # while N > 0:
# #     ans = input()
# #     N -= 1
# #     ans = list(ans.split())
# #
# #     if ans[0] == "insert":
# #         List.insert(int(ans[1]), int(ans[2]))
# #     elif ans[0] == "append":
# #         List.append(int(ans[1]))
# #     elif ans[0] == "remove":
# #         List.remove(List[1])
# #     elif ans[0] == "sort":
# #         List.sort()
# #     elif ans[0] == "pop":
# #         List.pop()
# #     elif ans[0] == "reverse":
# #         List.reverse()
# #     else:
# #         print(List)
#
#
# # ===================================================================
# # def findSubString(String, subString):
# #     count = 0
# #     for i in range(len(String) - len(subString) + 1):
# #         if String[i: i + len(subString)] == subString:
# #             count += 1
# #     return count
# #
# #
# # string = input().strip()
# # sub_string = input().strip()
# #
# # count = findSubString(string, sub_string)
# # print(count)
# # ==================================================================
# #
# # def isalnum(string):
# #     for i in str(string ):
# #         if i.isalnum():
# import os
# from functools import reduce
#
#
# def swap_case(s):
#     return s.swapcase()
#
#
# # s = input()
# # result = swap_case(s)
# # print(result)
#
#
# def split_and_join(line):
#     return "-".join(line.split())
#
#
# # if __name__ == '__main__':
# # line = input()
# # result = split_and_join(line)
# # print(result)
#
# # lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
# # string = "abracadabra"
# # string = string[:5] + "k" + string[6:]
# # print(string)
#
#
# def mutate_string(string, position, character):
#     l = list(string)
#     l[position] = character
#     string = ''.join(l)
#     return string
#
#
# # print(mutate_string("abracadabra", 5, "k"))
#
# # s = input()
#
# # print(any([char.isalnum() for char in s]))
# # print(any([char.isalpha() for char in s]))
# # print(any([char.isdigit() for char in s]))
# # print(any([char.islower() for char in s]))
# # print(any([char.isupper() for char in s]))
#
#
# ===========================================================================================

# from cmath import phase

# # complexNumber = complex(input())
# # z = complexNumber.real ** 2 + complexNumber.imag ** 2
# # print(z ** 0.5)
# # print(phase(complex(complexNumber.real, complexNumber.imag)))
## ===========================================================================================

# # a = int(input())
# # b = int(input())
# # c = int(input())
# # d = int(input())
# # z = (pow(a, b) + pow(c, d))
# # print(z)
## ===========================================================================================

# # 1
# # 22
# # 333
# # 4444
# # for row in range(1, int(input())):
# #     print(row * (pow(10, row) -1 ) // 9)

# ===========================================================================================

# # myList1 = []
# # mySet = {""}
# # mySet.clear()
# # i = int(input())
# # for s in range(0, i):
# #     mySet.add((map(int, input().split(" "))))
# def average(array):
#     return sum(set(array)) / len(set(array))


# ===========================================================================================
# def M(m):
#    return set(m)

# if __name__ == '__main__':
#     n1 = int(input())
#     arr1 = list(map(int, input().split()))
#     a = M(arr1)
#     n2 = int(input())
#     arr2 = list(map(int, input().split()))
#     b = M(arr2)
#     myList = []
#     myListSort = []
#
#     for s in a.symmetric_difference(b):
#         myList.append(s)
#         myList.sort()
#
#     for my_list_sort in myList:
#         print(my_list_sort)
# ===========================================================================================
# frCourse = input()
# n = int(input())
# s = set(map(int, input().split()))
# for i in range(int(input())):
#     string = input().split()
#     if string[0] == 'pop':
#         s.pop()
#     elif string[0] == 'remove':
#         s.remove(int(string[1]))
#     elif string[0] == 'discard':
#         s.discard(int(string[1]))
# print(sum(s))
# ===========================================================================================
# def solve(meal_cost, tip_percent, tax_percent):
#     # Write your code here
#     tip = float((tip_percent / 100) * meal_cost)
#     tax = float((tax_percent / 100) * meal_cost)
#     total_cost = meal_cost + tip + tax
#     return round(total_cost)

# #
# if __name__ == '__main__':
#     meal_cost = float(input().strip())
#
#     tip_percent = int(input().strip())
#
#     tax_percent = int(input().strip())
#
#     print(solve(meal_cost, tip_percent, tax_percent))

# =============================================================================
#  Print a string literal saying "Hello, World." to stdout.

# input_string = input()
# print(f'Hello, World.\n{input_string}')

# i, d, s = 4, 4.0, 'HackerRank '
# ii = int(input())
# dd = float(input())
# ss = str(input()).strip()
# print(ii + i)
# print(dd + d)
# print(s+ss)
# ===========================================================================================

# if __name__ == '__main__':
#     for _ in range(int(input())):
#         name = input()
#         score = float(input())

# def secondLowestGrade(classList):
#     secondLowestScore = sorted(set(_[1] for _ in classList))[1]
#     result = sorted([_[0] for _ in classList if _[1] == secondLowestScore])
#     return result

# ========================or===================================================================
# classList = []
# classListMarks = []
# classListMarksCopy = []
# myList = []
#
# for _ in range(int(input())):
#     classList.append([input(), float(input())])
#
# for n in range(len(classList)):
#     classListMarks.insert(n, classList[n][1])
#
# classListMarksCopy = classListMarks.copy()
# m = min(classListMarks)
#
# for _ in range(classListMarks.count(m)):
#     classListMarks.remove(m)
#
# m2 = min(classListMarks)
#
# for _ in range(len(classList)):
#     if classListMarksCopy[_] == m2:
#         myList.append(classList[_][0])
#
# myList.sort()
# for _ in range(len(myList)):
#     print(myList[_])

# ===========================================================================================

# List = []
# n = int(input())
# while len(List) < n:
#     List.extend((map(int, input().split())))
#
# m = max(List)
# for n in range(List.count(m)):
#
# print(max(List))

# ============================================================================================
# x = int(input())
# y = int(input())
# z = int(input())
# n = int(input())
#
# listOfAnswers = []
# for i in range(x + 1): # 2
#     for j in range(y + 1):# 2
#         for k in range(z + 1): # 2
#             if i + j + k != n:
#                 listOfAnswers.append([i, j, k])
#
# print(listOfAnswers)
# =================================================================================
# if __name__ == '__main__':
#     n = int(input())
#     student_marks = {}
#     for _ in range(n):
#         name, *line = input().split()
#         scores = list(map(float, line))
#         student_marks[name] = scores
#     query_name = input()
#     print(f"{sum(student_marks[query_name]) / len(student_marks[query_name]):.2f}")

# =================================================================================
import hashlib
# myTuple = []
# n = int(input())
# while len(myTuple) < n:
#     myTuple.extend(tuple(map(int, input().split())))
# print(hash(myTuple))
# #  ========or========
# n = int(input())
# print(hash(tuple(map(int, input().split()))))

# n = int(input())
# integer_list = tuple(map(int, input().split()))
# print(hash(integer_list))
# =================================================================================
