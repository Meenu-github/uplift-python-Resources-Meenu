leap_year = int(input("Enter the year: "))
def leap(year):
    leapyear = False
    if (year%400==0):
        if year%100==0:
            leapyear = True
        else:
            leapyear = False
    elif year%4==0:
        leapyear = True
    return leapyear
test_year = leap(leap_year)
if test_year == True:
    print(str(leap_year) + " is a leap year.")
else:
    print(str(leap_year)+ " is not a leap year.")


