mylist = [0, 1, 1, 2, 3, 4, 4, 4, 5]

newlist = []

for number in mylist:
    if number not in newlist:
        newlist.append(number)

print(newlist)
