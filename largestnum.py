# find the largest number among five numbers
num = [0] * 5
i = 0
while i <= 4:
    num[i] = int(input("Enter number: "))
    i = i + 1

# finding largest number
largest = num[0]  # assume first number is largest
i = 1
while i <= 4:
    if num[i] > largest:  # check if the next number is largest
        largest = num[i]  # replace previous largest
    i = i + 1

print("Largest number is " + str(largest))
