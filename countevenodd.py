n=[1,2,5,4,7,6,9,34]
e=o=0
for i in n:
    if i%2 == 0:
        e=e+1
    else:
        o=o+1
print(f"even:{e}\n odd:{o}")