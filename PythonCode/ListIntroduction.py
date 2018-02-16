a = [3, 10, -1]
print(a)
a.append(2)
print(a)
a.append('Hello')
print(a)
a.append([6,4])
print(a)
a.pop()
print(a)
a.pop()
print(a)
print(a[0])
print(a[3])
a[0] = 15
print(a)
b = ['Bannana','Apple','Microsoft']
print(b)
temp = b[0]
b[0] = b[2]
b[2] = temp
print(b)
print('Shortcut')
b[0],b[2] = b[2], b[0]
print(b)
