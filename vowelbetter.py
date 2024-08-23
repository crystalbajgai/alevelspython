vowels = ['a', 'e', 'i', 'o', 'u']

name = input("Enter your name: ")
i = 0
while i <= len(name) - 1:
    a = name[i].lower()
    if a in vowels:
        print(a)
    i = i + 1
