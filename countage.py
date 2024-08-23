age = [] * 10
a1520c = 0
a3040c = 0
a5060c = 0


for i in range(10):
    age[i] = int(input("Enter your age: "))
    if age[i] > 14 and age[i] < 21:
        a1520c = a1520c + 1
    elif age[i] > 29 and age[i] < 41:
        a3040c = a3040c + 1
    elif age[i] > 49 and age[i] < 60:
        a5060c = a5060c + 1

print("15 to 20: ", a1520c)
print("30 to 40: ", a3040c)
print("50 to 60: ", a5060c)
