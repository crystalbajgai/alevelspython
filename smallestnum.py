# find the smallest number among five numbers
num = [0] * 5
i = 0
while i <= 4:
    num[i] = int(input("Enter number: "))
    i = i + 1

# finding smallest number
smallest = num[0]  # assume first number is smallest
i = 1
while i <= 4:
    if num[i] < smallest:  # check if the next number is smallest
        smallest = num[i]  # replace previous smallest
    i = i + 1

print("Smallest number is " + str(smallest))
