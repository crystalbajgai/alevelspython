# 3. input a string and remove space
# 4. input n and display total sum of all numbers from 1 to n.
# 5. input a string, a char and count total accurance of given char in given string.
# given string. example: string = rama char =a total a is 2 (exam questions)

def spr(text):
    newtext = ''
    i = 0
    while i < len(text):
        if text[i] == ' ':
            newtext = newtext
        else:
            newtext = newtext + text[i]
        i = i + 1
    return newtext


string = input("Enter string with space: ")
print(spr(string))
