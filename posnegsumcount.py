#input any 10 number and display total sum and total count of positive and negative separately

countp = 0
countn = 0
sump = 0
sumn = 0

for i in range(10):
    num = int(input("Enter number: "))
    if num > 0:
        countp+=1
        sump = sump + num
    elif num < 0:
        countn+=1
        sumn = sumn + num
    else:
        print("Please enter a positive or negative number.")

print("Positive numbers:", countp)
print("Negative number:", countn)
print("Sum of positive numbers:", sump)
print("Sum of negative numbers:", sumn)