# exam question
# input a number and a character
# contact (join) given character given number of times
# eg num = 3 char = z then output is zzz

num = int(input("Enter a number: "))
char = input("Enter a character: ")
newchar=''

i = 0
while i < num:
    newchar = newchar + char
    i = i+1
print(newchar)

