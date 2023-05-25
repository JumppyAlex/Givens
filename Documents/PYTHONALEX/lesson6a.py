#Program to find if year is leap or not 
year = int(input('Enter a year ?:'))
if year %4 == 0 and year%100 == 0 and year%400 == 0:
    print('Year is leap')

elif year%4 == 0 and year%100 == 0 and year%400 == 0:
    if year%400==0:
        print("Year is leap 2")
    else:
        print('Not leap year')

else:
    print("Not leap year")

