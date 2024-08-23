# replace a with @ and e with # in a given string and return new string

def replacer():
    newtext = ""
    text = input("Enter string: ")
    i = 0
    while i < len(text):
        onechar = text[i]
        if onechar == 'a':
            newtext = newtext + '@'
        elif onechar == 'e':
            newtext = newtext + '#'
        else:
            newtext = newtext + onechar
        i = i + 1
    return newtext


print(replacer())
