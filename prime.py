def prime(n):
    f=0
    for i in range(2,n//2):
        if n%i == 0:
            f=1
            break
    if f==1:
        print("not Prime")
    else :
        print("prime")
n= int(input("enter Number"))
prime(n)