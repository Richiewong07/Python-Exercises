# def square(num):
#     return num ** 2
#
# results = square(3)
#
# print(results)


# square = lambda num: num ** 2
#
# print(square(3))



# def square(num):
#     return num**2
#
# my_nums = [1, 2, 3, 4, 5]
#
# for item in map(square, my_nums):
#     print(item)
#
# print(list(map(square,my_nums)))


mynums = [1, 2, 3, 4, 5, 6]
print(list(map(lambda num: num**2, mynums)))



# def check_even(num):
#     return num%2 == 0
#
# mynums = [1, 2, 3, 4, 5, 6]
#
# results = list(filter(check_even, mynums))
#
# print(results)

print(list(filter(lambda num: num%2 ==0, mynums)))



names = ['Andy', 'Eve', 'Sally']
print(list(map(lambda x:x[::-1], names)))
