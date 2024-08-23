# 2. input n and count total number of even from 1 to n


def total(n):
    count = 0
    i = 1
    while i <= n:
        if i % 2 == 0:
            count = count + 1
        i = i + 1
    return count

num = int(input("Enter number: "))
print("The total even numbers are: ", total(num))