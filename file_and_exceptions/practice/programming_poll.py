# Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

file_name = 'programming_poll.txt'
responses = []

while True:
    response = input("Why do you like programming: ")
    responses.append(response)

    continue_poll = input("Would you like someone else to respond (Y or N): ")
    if continue_poll != 'Y':
        break

with open(file_name, 'a') as file_object:
    for response in responses:
        file_object.write(response + "\n")
