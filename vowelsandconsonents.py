# input any string and count each vowels and total consonant. (Assume there is no space.)

# input any string and count total vowels and consonants. (Space shouldn't be counted.)

countv = 0  # for vowels
countc = 0  # for consonants
a = 0
e = 0
i = 0
o = 0
u = 0

mystring = input("Enter any string: ")
n = 0
while n <= len(mystring) - 1:
    onechar = mystring[n].lower()
    if onechar == "a":
        a = a + 1
    elif onechar == "e":
        e = e + 1
    elif onechar == "i":
        i = i + 1
    elif onechar == "o":
        o = o + 1
    elif onechar == "u":
        u = u + 1
    elif onechar != ' ':
        countc = countc + 1
    # end if
    n = n + 1

print("Total a = " + str(a))
print("Total e = " + str(e))
print("Total i = " + str(i))
print("Total o = " + str(o))
print("Total u = " + str(u))
print("Total consonant = " + str(countc))
