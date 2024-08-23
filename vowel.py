# input a name and check if it starts with vowel

name = input("Enter your name: ")
char = name[0]
if char.lower() == "a" or char.lower() == "e" or char.lower() == "i" or char.lower() == "o" or char.lower() == "u":
    print(f"Your name {name} starts with vowel.")
else:
    print(f"Your name {name} doesn't start with vowel.")
