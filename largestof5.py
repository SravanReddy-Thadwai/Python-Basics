largest=float(input("enter 1st no."))
for i in range(2,6):
    num=float(input(f"enter {i} number"))
    if num>largest:
        largest = num

print("\n the largest number is ",largest)