#input any 10 numbers and display average of odd and even numbers separately (must've one odd and even atleast)

counte = 0
counto = 0
sumo = 0
sume = 0

for i in range(10):
    num = int(input("Enter number: "))
    if num % 2 == 0:
        counte = counte + 1
        sume = sume + num
    else:
        counto = counto + 1
        sumo = sumo + num

print("Average of even:", sume/counte)
print("Average of odd:",sumo/counto)