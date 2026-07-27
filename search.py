n=[1,3,2,4,56,54,0]
s=int(input("enter search element"))
for i in n:
    if i==s:
        print(f"{s} found")
        break

if i!=s:
     print("not found")