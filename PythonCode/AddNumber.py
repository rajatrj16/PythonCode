value=1
summ=0
print("Enter Numbers to add to the sum")
print("Enter 0 to quit.")
while value !=0:
    print("Current Sum: ",summ)
    value=int(input("Enter Number? "))
    summ+=value
    print("---")
print("Total Sum is: ",summ)
    
