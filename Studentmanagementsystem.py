s={}
m=[]
s["name"]=input("enter name")
s["roll"]=int(input("enter roll no"))
for i in range(5):
    m.append(float(input(f"enter {i+1} subject marks ")))
s["marks of 5 sub"]=m
for key,value in s.items():
    print(f"{key}:{value}")
print("total marks",sum(m))
print("average marks",sum(m)/len(m))
a=sum(m)/len(m)
if a>= 90:
    print("Grade is A")
elif a >= 80:
    print("Grade is B")
elif a >=70:
    print("Grade is C ")
elif a>=50: 
    print("Pass")
else:
    print("Fail")