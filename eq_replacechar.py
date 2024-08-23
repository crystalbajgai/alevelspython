# input fullname and replace 'a' with '#' and 'm' with 'a' (Exam question)
# eg anita  should be #nit#

newtext = ""  # this is empty
mytext = input("Enter fullname: ")
i = 0
while i <= len(mytext) - 1:
    onechar = mytext[i]
    if onechar == "a":
        newtext = newtext + '#'
    elif onechar == "m":
        newtext = newtext + '@'
    else:
        newtext = newtext + onechar
    i = i + 1
print(newtext)
