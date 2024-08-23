# qn 2 solution
num = [0] * 5  # defining array
evensum = 0
evencount = 0
oddsum = 0
oddcount = 0

i = 0
while i <= 4:
    num[i] = int(input("Enter number: "))
    if num[i] % 2 == 0:
        evensum = evensum + num[i]
        evencount = evencount+1
    else:

        oddsum = oddsum + num[i]
        oddcount = oddcount+1
    i = i + 1

print("Even sum = " + str(evensum))
print("Even Average = " + str(evensum/evencount))
print("Odd sum = " + str(oddsum))
print("Odd Average = " + str(oddsum/oddcount))
