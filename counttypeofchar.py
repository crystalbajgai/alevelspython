# imput any string and count total captial letter, small letter and digits.

countc = 0  # for captial
counts = 0  # for small
countd = 0  # for digit

mystring = input("Enter any string: ")
i = 0
while i <= len(mystring) - 1:
    onechar = mystring[i]
    if onechar >= "A" and onechar <= "Z":
        countc = countc + 1
    elif onechar >= "a" and onechar <= "z":
        counts = counts+1
    elif onechar >= "0" and onechar <= "9":
        countd = countd + 1

    i = i+1
print("Total captial = " + str(countc))
print("Total small = " + str(counts))
print("Total digit = " + str(countd))
