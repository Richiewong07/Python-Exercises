with open('write.txt', mode='w') as f:
    f.write('I CREATED THIS FILE!')

with open('write.txt', mode='r') as f:
    print(f.read())
