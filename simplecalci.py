print("----simple Calcculator----")
num1=int(input("enter first no."))
num2=int(input("enter 2nd no."))
print("\nResults")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Division: Cannot divide by zero")