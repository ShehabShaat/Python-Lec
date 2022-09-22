

# str()
a = 10 
print(type(a))
print(str(a))
print(type(str(a)))

# tuple()

c = "shehab" # String
d = [1,2,3,4,5] # List
e = {"A" , "B" , "C"} # Set
f= {"A":1,"B":2} # Dict


print(tuple(c))
print(tuple(d))
print(tuple(e))
print(tuple(f))
# print(tuple(500))  Error 'int' object is not iterable
print("="*50)
# List()
c = "shehab" # String
d = (1,2,3,4,5) # Tuple
e = {"A" , "B" , "C"} # Set
f= {"A":1,"B":2} # Dict


print(set(c))
print(set(d))
print(set(e))
print(set(f))

print("="*50)

# set()
c = "shehab" # String
d = (1,2,3,4,5) # Tuple
e = ["A" , "B" , "C"] # list
f= {"A":1,"B":2} # Dict


print(set(c))
print(set(d))
print(set(e))
print(set(f))
print("="*50)


# dict()
d = (("A",1),("B",2),("c",3)) # Tuple
e = [["A",1],["B",2],["C",3]] # list

print(dict(d))
print(dict(e))

