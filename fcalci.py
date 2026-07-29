def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if a>b:
        return a/b
    else:
        print("not possible")
while True :
    print("\n === calculator====")
    print("1.add 2.sub,3.mul,4.div,5.exit")
    c=int(input("enter choice 1-5"))
    if c ==5:
        print("thank you")
        break
    if c>=1 and c<=4:
        a= int(input("enter 1st no."))
        b=int(input("enter 2nd no."))
        if c==1:
            print(add(a,b))
        elif c==2:
            print(sub(a,b))
        elif c==3:
            print(mul(a,b))
        elif c==4:
            print(div(a,b))
    else:
        print ("invalid choice")
