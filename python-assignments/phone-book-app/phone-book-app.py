import json


def look_up():
    name = input("What is the person's name: ").capitalize()

    with open('phone_book.json', 'r') as file_handle:
        contacts = json.load(file_handle)
        # print(contacts[name])
        print(contacts.get(name, 'Name not found'))




def main():
    print('Electronic Phone Book')
    print('1. Look up an entry \n2. Set an entry \n3. Delete an entry \n4. List all entries \n5. Quit')

    user_input = int(input('Enter Number (1-5): '))

    while True:
        if user_input == 1:
            look_up()
        elif user_input == 2:
            print(2)
        elif user_input == 3:
            print(3)
        elif user_input == 4:
            print(4)
        elif user_input == 5:
            print(5)
        break





if __name__ == '__main__':
    main()
