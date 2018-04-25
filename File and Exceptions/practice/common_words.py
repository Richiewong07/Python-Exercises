
filename = 'row.txt'

with open(filename) as file_object:
    content = file_object.read()
    common_words = content.lower().count('row')
    print('The word row appears {} in the song.'.format(common_words))
