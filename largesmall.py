# display largest among three number.

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
if x > y and x > z:
    print(str(x) + " is largest.")
elif y > x and y > z:
    print(str(y) + " is largest.")
elif z > x and z > y:
    print(str(z) + " is largest.")

# display smallest among three number.

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a < b and a < c:
    print(str(a) + " is largest.")
elif b < a and b < c:
    print(str(b) + " is largest.")
elif c < a and c < b:
    print(str(c) + " is largest.")
