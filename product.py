# input any 3 numbers and display their product
# use function with arugument and parameter

def prod(x, y, z):
    prod = x * y * z
    print("Total prod is " + str(prod))


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))


prod(a, b, c)
