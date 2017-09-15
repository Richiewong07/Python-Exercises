height = int(input('Height?'))
width = int(input('Width?'))


# draw the top border
print ('*' * width)

# draw the middle with side border and spaces in middle
number_spaces = width - 2
spaces = ' ' * number_spaces

for i in range(height - 2):
    print('*' + spaces + '*')

# draw the bottom border
print ('*' * width)
