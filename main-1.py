# Leap year

def isLeapyear(year):
 if (year%4==0):
   return True
 else:
   return False

year=int(input("enter a year :"))

if isleapyear(year):
  print("{} is leap year.".format (year));
else:
  print("{} is not leap year.".format (year));