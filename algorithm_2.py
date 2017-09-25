my_list = list(range(0, 1000))
sum = 0

for i in my_list:
    if i %3 == 0 or i %5 == 0:
        sum += i

print(sum)
