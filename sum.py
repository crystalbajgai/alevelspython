# return sum of all even numbers between 1 to 100

def sume():
    sum_even = 0
    num = 1
    while num <= 100:
        if num % 2 == 0:
            sum_even = sum_even + num
        num = num + 1
    return sum_even
result = sume()
print("Sum of even numbers between 1 and 100:", result)
