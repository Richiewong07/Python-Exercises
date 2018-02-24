# OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

def old_macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'

results = old_macdonald('macdonald')
print(results)


# MASTER YODA: Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    return ' '.join(text.split()[::-1])

results = master_yoda('I am home')
print(results)


# ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200

def almost_there(n):
    return((abs(100 - n) <= 10) or (abs(200 - n) <= 10))

results = almost_there(90)
print(results)
