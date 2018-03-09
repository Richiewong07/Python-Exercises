# Prompt the user for two things:
#
# The total bill amount:
# The level of service, which can be one of the following: good, fair, or bad
# Calculate the tip amount and the total amount (bill amount + tip amount).
# The tip percentage based on the level of service is based on:
#
# good -> 20%
# fair -> 15%
# bad -> 10%

input_amount = int(input('Enter cost of the bill: '))
input_service = input('Enter level of service (Good, Fair, Bad): ').capitalize()

def tip_percentage(cost, service):
    if service == 'Good':
        tip = 0.20
    elif service == 'Fair':
        tip = 0.15
    elif service == 'Bad':
        tip = 0.10

    total_cost = cost + (cost * tip)
    return total_cost

total_bill = tip_percentage(input_amount, input_service)
print('Your total bill is ${}.'.format(total_bill))
