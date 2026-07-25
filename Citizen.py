name=input("enter your Name")
age=int(input("enter Age"))
if age>= 60:
    print("Senior Citizen")
elif age>=20 and age<=59 :
    print("adult")
elif age<=19 and age>=13:
    print("Teenager")
else:
    print("Child")
    