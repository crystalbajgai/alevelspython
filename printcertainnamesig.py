#prints name starting with a or d
name = [""] * 5
ad = ["a", "d"]
tp = []


for i in range(5):
    name[i] = input("Enter name: ")
    if name[i][0] in ad:
        tp.append(name[i])

for j in range(len(tp)):
    print("")
    print(tp[j])
