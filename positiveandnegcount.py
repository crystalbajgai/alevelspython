# qn 3 solution
num = [0] * 10  # defining array
pcount = 0
ncount = 0
z = 0


i = 0
while i < 10:
    num[i] = int(input("Enter number: "))
    if num[i] > 0:
        pcount = pcount + 1
    elif num[i] < 0:
        ncount = ncount + 1
    else:
        z = z + 1
    i = i + 1

print("Total positive number is: ", pcount)
print("Total negative number is: ", ncount)
print("Total zero is: ", z)
