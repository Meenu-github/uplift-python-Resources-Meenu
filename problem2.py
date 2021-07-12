leap_year = int(input("Enter the year : "))
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
print(leap(leap_year))
