#input any number and check if it is odd or even


def oe(x):
    if x % 2 == 0:
        print("The number is even.")
    else:
        print("It is odd.")


a = int(input("Enter number: "))
oe(a)
