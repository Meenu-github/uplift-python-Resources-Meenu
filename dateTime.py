import datetime

x = datetime.datetime.now()

#print year
print(x.year)
#print day
print(x.strftime("%A"))
#print day in short form
print(x.strftime("%a"))
#print month
print(x.strftime("%B"))

# print month in short form
print(x.strftime("%b"))

#print local version of date
print(x.strftime("%x"))
#print local version of time
print(x.strftime("%X"))
#print year short version
print(x.strftime("%y"))
#print time
print(x.time())
#print date
print(x.date())
# print month in number
print(x.month)
