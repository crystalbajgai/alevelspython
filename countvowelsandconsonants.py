# input any string and count total vowels and consonants. (Space shouldn't be counted.)

countv = 0  # for vowels
countc = 0  # for consonants

mystring = input("Enter any string: ")
i = 0
while i <= len(mystring) - 1:
    onechar = mystring[i].lower()
    if onechar == "a" or onechar == "e" or onechar == "i" or onechar == "o" or onechar == "u":
        countv = countv + 1
    elif onechar != ' ':
        countc = countc + 1
    #end if
    i = i + 1

print("Total vowels = " + str(countv))
print("Total consonant = " + str(countc))