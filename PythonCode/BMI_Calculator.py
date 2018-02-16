#BMI_Calculator Which shows that you are perfect with your height and weight or not!
name = input('Enter Name: ')
height_m = float(input('Enter Height in meters: '))
weight_kg = float(input('Enter Weight in KGs: '))

bmi = weight_kg / (height_m ** 2)
print('BMI: ')
print(bmi)
if(bmi < 25):
     #print(name)
     print('Hey '+name,'You are Perfect :)')
else:
    print(name)
    print('Sorry '+name,'you are overweighted')
    print(" ")
i = input('Press anything to Exit!')
    

