phonebook = {
  'Alice': '703-493-1834',
  'Bob': '857-384-1234',
  'Elizabeth': '484-584-2923'
}


def look_up():
    person_name = input("What is the person's name: ").upper()




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
