import json


# 1. If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.

def look_up():
    name = input("What is the person's name: ").capitalize()

    with open('phone_book.json', 'r') as file_handle:
        contacts = json.load(file_handle)
        # print(contacts[name])
        print(contacts.get(name, 'Name not found'))

# 2. If they choose to set an entry, you will prompt them for the person's name and the person's phone number,

def set_entry():

    contacts = {}

    name = input("Enter name: ").capitalize()
    contacts[name] = {"phone": None, "email": None, "URL": None}

    phone = input("Enter phone number (XXX-XXX-XXX): ")
    contacts[name]['phone'] = phone
    # email = input("Enter email: ")
    # url = input("Enter URL")

    with open('phone_book.json', 'w') as file_handle:
        json.dump(contacts, file_handle)

# 3. If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.

def delete_entry():
    pass

# 4. If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.

def list_all():
    pass

# 5. If they choose to quit, end the program.

def quit():
    pass



def main():
    print('Electronic Phone Book')
    print('1. Look up an entry \n2. Set an entry \n3. Delete an entry \n4. List all entries \n5. Quit')

    user_input = int(input('Enter Number (1-5): '))


    while True:
        if user_input == 1:
            look_up()
        elif user_input == 2:
            set_entry()
        elif user_input == 3:
            print(3)
        elif user_input == 4:
            print(4)
        elif user_input == 5:
            print(5)
        break





if __name__ == '__main__':
    main()
