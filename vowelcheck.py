vowels = ['a', 'e', 'i', 'o', 'u']

name = input("Enter your name: ")

if name[0].lower() in vowels:
    print("Your name starts with vowel.")
else:
    print("Your name doesn't start with vowel.")
