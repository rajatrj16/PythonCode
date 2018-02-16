month_days = [0,31,28,31,30,31,30,31,31,30,31,30,31]

def leap_year(year):
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
    print('This year is leap year: ')


def days_in_month(year,month):
    
    if not 1 <= month <= 12:
        return 'Invalid Month'
    
    if month == 2 and leap_year(year):
        return 'This month have 29 days: '
    
    return month_days(month)

year = int(input('Enter Year: '))
month= int(input('Enter Month: '))

print(days_in_month(year,month))
