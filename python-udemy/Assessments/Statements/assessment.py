# Use for, .split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'

for word in st.split():
    if word[0].lower() == 's':
        print(word)


# Use range() to print all the even numbers from 0 to 10.

print(list(range(0, 11, 2)))


# Use a List Comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

print([x for x in range(1, 51) if x % 3 == 0])


# Go through the string below and if the length of a word is even print "even!"

st2 = 'Print every word in this sentence that has an even number of letters'

for word in st2.split():
    if len(word) % 2 == 0:
        print(word)
