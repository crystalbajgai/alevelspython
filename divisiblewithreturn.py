# count how many numbers between 1 to 100 which are divisible by 5 and return

def divisible():
    count = 0
    num = 1
    while num <= 100:
        if num % 5 == 0:
            count = count + 1
        num = num + 1
    return count
result = divisible()
print("Divisible by 5 between 1 and 100:", result)
