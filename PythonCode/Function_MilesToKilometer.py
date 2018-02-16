miles = float(input('Enter Miles: '))
print('Miles: ')
print(miles)
print(' ')
def convert(miles):
    print('Converting Miles to Kilometer: ')
    return 1.60934 * miles
km = convert(miles) 
print(km)
