def ask_for_int():
    while True:
        try:
            result = int(input('Please provide number: '))
        except:
            print('Whoops! That is not a number')
            continue
        else:
            print('Yes thank you')
            break
        # finally:
        #     print("I'm going to ask you again! \n")

ask_for_int()
