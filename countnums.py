# input any five number and count as follows.
# how many between 10 to 20
# how many between 50 to 70
# how many between 80 to 100

c1 = 0
c2 = 0
c3 = 0


for i in range(5):
    num = int(input("Enter any number: "))
    if num > 9 and num < 20:
        c1 = c1 + 1
    elif num > 49 and num < 71:
        c2 = c2 + 1
    elif num > 79 and num < 101:
        c3 = c3 + 1

print("Between 10 to 20: ", c1)
print("Between 50 to 70: ", c2)
print("Between 80 to 100: ", c3)
