my_list = list(range(1, 101))
my_list_2 = []
print(my_list_2)

for i in my_list:
    if i %3 == 0 and i %5 == 0:
        my_list_2.append('FizzBuzz')
    elif i %3 == 0:
        my_list_2.append('Fizz')
    elif i %5 == 0:
         my_list_2.append('Buzz')
    else:
        my_list_2.append(i)
    i += 1
print(my_list_2)
