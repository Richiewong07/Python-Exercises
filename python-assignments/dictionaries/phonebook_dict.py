# Given the following dictionary, representing a mapping from names to phone numbers:

# phonebook_dict = {
#   'Alice': '703-493-1834',
#   'Bob': '857-384-1234',
#   'Elizabeth': '484-584-2923'
# }

# Write code to do the following:
#
# Print Elizabeth's phone number.
# Add a entry to the dictionary: Kareem's number is 938-489-1234.
# Delete Alice's phone entry.
# Change Bob's phone number to '968-345-2345'.
# Print all the phone entries.


phonebook = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}

def main():
    # Print Elizabeth's phone number.
    print(phonebook['Elizabeth'])

    # Add a entry to the dictionary: Kareem's number is 938-489-1234.
    phonebook['Kareem'] = '938-489-1234'

    # Delete Alice's phone entry.
    del phonebook['Elizabeth']

    # Change Bob's phone number to '968-345-2345'.
    phonebook['Bob'] = '968-345-2345'

    # Print all the phone entries.
    print(phonebook)



if __name__ == '__main__':
    main()
