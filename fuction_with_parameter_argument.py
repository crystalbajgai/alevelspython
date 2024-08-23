# function with argument and parameter
# note:
# do not take input inside function
# rest code is usual coding
# example 1
# display sum of two integer using argument and parameter

def add(x, y): #here x and y are parameter
    sum = x + y
    print("Total sum is " + str(sum))
# end def


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

add(a, b)  # calling function with argument a, b
