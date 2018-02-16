n=int(input("Enter number ? "))
if n < 0:
    print("The Absolute value of",n,"is",-n)
else:
    print("The Absolute value of",n,"is",n)

print("Indentation is very much required")

print("----------(elif)--------")

name=input("Enter Name ? ")
if name=="mark":
    print("The name entered is ",name)
elif name=="john":
        print("The name entered is ",name)
elif name=="thor":
        print("The name entered is ",name)
else:
    print("Name entered is not valid")

print("--------------(Nested If)----------")

name="animal"
animalName="dogg"
if(name=="animal"):
    if(animalName=="dog"):
        print("valid animal")
    else:
        print("animal name is invalid")
    print("Name entred is animal")
else:
    print("not a valid name")
    
