# count how many vowels in a string and return

def vchecker():
    vc = 0
    v = ['a', 'e', 'i', 'i', 'o', 'u']
    string = input("Enter string: ")
    for i in range(len(string)):
        if string[i] in v:
            vc = vc + 1
    return vc


print(vchecker())
