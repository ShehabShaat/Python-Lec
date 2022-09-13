# zip() loop many iterators
# zip() return a zip object contain all object
# zip() length is a  length the lowest object
List1 = [1, 2, 3]
List2 = ["A", "B", "C", "E"]
Tuple1 = ("Man", "Women", "girl", "Boy")
dict1 = {"Name": "shehab", "Skills": "Python", "Age": "22"}

res = zip(List1, List2, Tuple1, dict1)
for item1, item2, item3, item4 in res:
    print("list 1 item=>", item1)
    print("list 2 item=>", item2)
    print("Tuple 1 item=>", item3)
    print("dict 1 key =>", item4, "dict 1 value =>", dict1[item4])
    print("="*50)
