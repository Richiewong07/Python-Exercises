# Allow the ability to divide the check into a equal parts amount a number of
# people. The user will enter the number of people to be divided amongst.


input_amount = int(input('Enter cost of the bill: '))
input_service = input('Enter level of service (Good, Fair, Bad): ').capitalize()
input_party = int(input('Enter number of people: '))

def tip_percentage(cost, service, party):
    if service == 'Good':
        tip = 0.20
    elif service == 'Fair':
        tip = 0.15
    elif service == 'Bad':
        tip = 0.10

    total_cost = format(cost + (cost * tip), '.2f')
    cost_per_person = format(total_cost / party, '.2f')

    print('The tip amount is ${}.\n Thetotal cost is ${}.\n The cost per person is ${}'.format(tip, total_cost, cost_per_person))

tip_percentage(input_amount, input_service, input_party)
