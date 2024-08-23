# input any number and display total sum from 1 to that given number
# example: if number is 5, then add 1 to 5 and display sum

def add(a):
    sum = 0
    for i in range(1, a+1):
        sum = sum + i
    print(sum)


b = int(input("Enter number to add upto: "))
add(b)
