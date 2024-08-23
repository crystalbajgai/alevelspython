
# minimu tc = 2 + 2 + 3

def ValidatePassword(Pass):
    tu = 0
    tc = 0
    tn = 0
    i = 0
    nay = 0
    for i in range(len(Pass)):
        if Pass[i] >= "a" and Pass[i] <= "z":
            tu = tu + 1
        elif Pass[i] >= "A" and Pass[i] <= "Z":
            tc = tc + 1
        elif Pass[i] >= '0' and Pass[i] <= '9':
            tn = tn + 1
        else:
            nay = nay + 1

    if tc > 1 and tu > 1 and tn > 2 and nay == 0:
        return True
    else:
        return False


pwd = input("Enter password: ")

num = ValidatePassword(pwd)
if num == True:
    print("The password is valid.")
else:
    print("The password is invalid.")
