#   # # #     #       #   # # # #   #       #     # # #     # # # #
# #           #       #   #         #       #   #       #   #       #
# #           #       #   #         #       #   #       #   #       #
#   # # #     # # # # #   # # # #   # # # # #   # # # # #   # # # #
#         #   #       #   #         #       #   #       #   #       #
#         #   #       #   #         #       #   #       #   #       #
#   # # #     #       #   # # # #   #       #   #       #   # # # #


for x in range(7):  # row
    for y in range(34):  # col
        if ((x == 0 or x == 3 or x == 6) and (0 < y < 4)) or (y == 4 and (3 < x < 6)) or (y == 0 and (0 < x < 3)) \
                or (y == 6 or y == 10) or x == 3 and (5 < y < 11) \
                or (y == 12) or ((x == 0 or x == 3 or x == 6) and (11 < y < 16)) \
                or (y == 17 or y == 21) or x == 3 and (16 < y < 22) \
                or ((y == 23 or y == 27) and (x > 0)) or (x == 0 and (23 < y < 27)) or x == 3 and (22 < y < 27) \
                or (y == 29) or ((x == 0 or x == 3 or x == 6) and (28 < y < 33)) or ((y == 33) and (0 < x < 3)) or ((y == 33) and ( 3 < x < 6)):

            print("# ", end="")
        else:
            print(end="  ")

    print()
