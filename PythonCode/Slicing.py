myList=[1,2,3,4,5,6,7,8,9,10,11,12]
print(myList)
print("Slicing--")
print(myList[6:10])

names=['a','b','c','d','e','f','g','h']
print(names)
print("Character Slicing--")
print(names[2:5])
print(names[2:])
print(names[:5])

print("Negative Index")
print(names[-2:])
print(names[:-5])
print(names)
print(names[:])


print("Skipping Values")
print(myList[2:12:2])
print(myList[::2])
print(myList[::-2])
