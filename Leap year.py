yr=int(input("Enter a year - ".format()))
x=yr%4
y=yr%400
z=yr%100
if((x==0 and z!=0) or (y==0)):
    print("This is a leap year.")
else:
    print("This is not a leap year.")