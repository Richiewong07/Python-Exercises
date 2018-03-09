# Allow the ability to divide the check into a equal parts amount a number of 
# people. The user will enter the number of people to be divided amongst.


total_bill = float(input('Total bill amount? '))
service = input('Level of service? ')
good = float(0.2 * total_bill)
fair = float(0.15 * total_bill)
bad = float(0.10 * total_bill)
good_bill = float(good + total_bill)
fair_bill = float(fair + total_bill)
bad_bill = float(bad + total_bill)
number_of_people = float(input('Total number of people? '))
total_amount_good_bill = float(good_bill / number_of_people)
total_amount_fair_bill = float(fair_bill / number_of_people)
total_amount_bad_bill = float(bad_bill / number_of_people)
if service == 'good':
    print('Tip amount: {:0.2f}'.format(good))
    print('Total amount: {:0.2f}'.format(good_bill))
    print('Amount per person: {:0.2f}'.format(total_amount_good_bill))
elif service == 'fair':
    print('Tip amount: {:0.2f}'.format(fair))
    print('Total amount: {0.2f}'.format(fair_bill))
    print('Amount per person: {:0.2f}'.format(total_amount_fair_bill))
elif service == 'bad':
    print('Tip amount: {:0.2}'.format(bad))
    print('Total amount: {:0.2f}'.format(bad_bill))
    print('Amount per person: {:0.2f}'.format(total_amount_bad_bill))
