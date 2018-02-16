#Use of lambda function

mylist = [1,2,3,4,5,6,7,8,9,10]
evens = filter(lambda num: num%2==0,mylist)
print(list(evens))
