a = ["Bannana","Apple","Microsoft"]
print(a)
print(a[0])
print(a[1])
print(a[2])
for element in a:
    print(element)
    print(element)
print(" ")



b = [10,20,30]
total = 0
for e in b:
    print(e)
    total = total + e
print("Sum is: ", total)

print(" ")




#1,2,3,4
c = list(range(1,5))
print(c)
print(" ")
total2 = 0
for i in range(1,11):
    print(i)
    total2 += i
print("Sum of first 10 Natural no is: ",total2)
print(" ")
print(list(range(1,30)))
total3 = 0
for i in range(1,31):
    if i % 3 == 0:
        total3 += i
        print(i)
print("Sum of Multiple of 3: ",total3)
print(" ")
print(" ")



#Compute all Multiple of 3 and 5 that are less than 100
print(list(range(1,101)))
total4 = 0
print("All the Values which are multiple of 3 and 5: ")
for i in range(1,101):
    if i % 3 == 0 | i % 5 == 0:
        print(i)
        total4 += i
print("Sum of multiple of 3 and 5 is: ",total4)
