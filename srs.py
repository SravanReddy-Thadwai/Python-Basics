s={}
s["name"]= input("enter Name")
s["roll no"]= int(input("enter roll no"))
s["Branch"]=input("enter Branch")
s["Branch"]="ECSE"
for key,value in s.items() :
    print(f"{key} : {value}")
    