# using argument, parameter and return
# 1. input string and count vowels

def vc(v):
    i = 0
    vcount = 0
    while i < len(v):
        onechar = v[i]
        if onechar == "a" or onechar == "e" or onechar == "i" or onechar == "o" or onechar == "u":
            vcount = vcount + 1
        i = i + 1
    return vcount


string = input("Enter string: ")
print("The number of vowels is:", vc(string))
