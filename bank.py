b=1000
def check():
    print(f"current balance is{b}")
def deposit(a):
    global b
    b=b+a
    print(f"{a}deposited successfully")
    check()
def withdraw(a):
    global b
    b=b-a
    print(f"{a} withdraw successfully")
    check()
check()
deposit(float(input("enter deposit amount")))
withdraw(float(input("enter withdraw amount")))
