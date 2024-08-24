#input any 5 number and display the largest number and also sum of all numbers excluding the largest one

large = 0
sum = 0
num = [0]*5

for i in range(5):
    num[i] = int(input("Enter number: "))
    
#finding largest number
for j in range(5):
    if num[j] > large:
        large = num[j]

#finding sum without the largest number
for k in range(5):
    if num[k] != large:
        sum = sum + num[k]

print("Largest number is:",large)
print("Sum excluding the largest:", sum)