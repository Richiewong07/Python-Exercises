# Write a program that will prompt you for how many coins you want. 
# Initially you have no coins. It will ask you if you want a coin?
# If you type "yes", it will give you one coin, and print out the current tally.
# If you type no, it will stop the program.


num_coins = 0
print('You have {} coins.'.format(num_coins))
while True:
    switch = input('Do you want another? (yes/no) ')
    if switch == 'yes':
        num_coins += 1
        print('You have {} coins.'.format(num_coins))
    elif switch == 'no':
        print('Bye')
        break
    else:
        print('Try again')
