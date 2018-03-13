height = 3


for i in range(height):
    spaces = height - i - 1
    stars = 2 * i + 1
    print (' ' * spaces + '*' * stars)
