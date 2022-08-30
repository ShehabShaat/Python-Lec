# # n = int(input())  # Number of elements
# # List = [int(elem) for elem in input().split(" ")]
# # print(List)
# # ==========================================================================
# # enCourse = int(input())
# # myList1 = list(map(int, input().split(" ")))
# #
# # frCourse = int(input())
# # myList2 = list(map(int, input().split(" ")))
# #
# # myList1 = set(myList1)
# # myList2 = set(myList2)
# # count = 0
# # for s in myList1.symmetric_difference(myList2):
# #     count += 1
#
# # print(count)
# # ===============================================================
# #  leap day
# # def is_leap(y):
# #     if y % 4 == 0:
# #         if y % 100 != 0:
# #             return True
# #         else:
# #             if y % 400 == 0:
# #                 return True
# #             else:
# #                 return False
# #     else:
# #         return False
# #
# #
# # year = int(input())
# # Output = bool(is_leap(year))
# # print(Output)
#
# # =========================================================

# List = []
# N = int(input())
# while N > 0:
#     ans = input()
#     N -= 1
#     ans = list(ans.split())
#
#     if ans[0] == "insert":
#         List.insert(int(ans[1]), int(ans[2]))
#     elif ans[0] == "append":
#         List.append(int(ans[1]))
#     elif ans[0] == "remove":
#         List.remove(List[1])
#     elif ans[0] == "sort":
#         List.sort()
#     elif ans[0] == "pop":
#         List.pop()
#     elif ans[0] == "reverse":
#         List.reverse()
#     else:
#         print(List)


# ===================================================================
# def findSubString(String, subString):
#     count = 0
#     for i in range(len(String) - len(subString) + 1):
#         if String[i: i + len(subString)] == subString:
#             count += 1
#     return count
#
#
# string = input().strip()
# sub_string = input().strip()
#
# count = findSubString(string, sub_string)
# print(count)
# ==================================================================
#
# def isalnum(string):
#     for i in str(string ):
#         if i.isalnum():


