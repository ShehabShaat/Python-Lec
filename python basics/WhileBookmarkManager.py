myFavouriteWeb = []
maximumWebs = 5
index = 0
while maximumWebs > 0:

    web = input("Website Name Without https:// : ").strip().lower()
    myFavouriteWeb.append(f"https://{web}")
    maximumWebs -= 1
else:
    print("Bookmark IS Full , you cant add more")

answer = input("Do you want to see your sBookmark ? Y or N :").strip().lower()

if answer == "yes" or answer == "y":
    myFavouriteWeb.sort()
    while index < len(myFavouriteWeb):
        print(myFavouriteWeb[index])
        index += 1
else:
    print("thanks for your time")
