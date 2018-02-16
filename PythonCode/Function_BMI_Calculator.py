#def function():
 #   print('Aaaaaa')
  #  print('Aaaaaa2')
#print('Outside Function')
#function()
#function()
#---------
#def function1(x):
 #   return 3*x
#a = function1(5)
#print(a)
#b = function1(7)
#print(b)
#print('sum:')
#print(a+b)
#---------

#BMI Calculator
name1 = input('Enter Name of first Person: ')
height_m1 = int(input('Enter Height in meters: '))
weight_kg1 = int(input('Enter Weight in Kilograms: '))
print('           ')
name2 = input('Enter Name of Second Person: ')
height_m2 = int(input('Enter Height in meters: '))
weight_kg2 = int(input('Enter Weight in Kilograms: '))
print('           ')
name3 = input('Enter Name of Third Person: ')
height_m3 = int(input('Enter Height in meters: '))
weight_kg3 = int(input('Enter Weight in Kilograms: '))
print('           ')
print(name1,height_m1,weight_kg1)
print(name2,height_m2,weight_kg2)
print(name3,height_m3,weight_kg3)
print('           ')
def bmi_calculator(name, height_m, weight_kg):
    bmi = weight_kg / (height_m ** 2)
    print('BMI: ')
    print(bmi)
    if bmi < 25:
        return name + ' is not overweight'
    else:
        return name + ' is overweight'
print('           ')
print('           ')
result1 = bmi_calculator(name1,height_m1,weight_kg1)
result2 = bmi_calculator(name2,height_m2,weight_kg2)
result3 = bmi_calculator(name3,height_m3,weight_kg3)
print('           ')
print('            ')
print('Results for BMI Calculators: ')
print('           ')
print(result1)
print(result2)
print(result3)
