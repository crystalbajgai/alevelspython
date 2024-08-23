# function with argument, parameter and return
# note:
# do not take input inside function
# and return result to out of the function
# add two numbers using argument, parameter and return

def add(x, y): #(here x,y are parameters)
    sum = x + y
    return sum
#end def

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
result = add(a, b)
print(result)
