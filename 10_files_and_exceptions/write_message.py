filename = 'text_files/programming.txt'

with open(filename, 'w') as file_object:    # OPEN FILE IN WRITE MODE
    file_object.write('I love programming.\n')
    file_object.write('I love createing new games.\n')
