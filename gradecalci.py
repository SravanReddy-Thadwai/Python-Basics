name=input("enter your name: ")
marks=int(input("enter your marks: "))
if marks>=90:
    print(name, "you got A grade")
elif marks >= 80:
    print("your  B grade ")
elif marks >= 70:
    print("your  c grade ")
elif marks >= 60:
    print("your  D grade ")
elif marks >= 50:
    print("your  P grade ")
else:
    print("fail")