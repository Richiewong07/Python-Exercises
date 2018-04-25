# try:
#     print(5/0)
# except ZeroDivisionError:   # except LOOKS FOR THE ERROR RAISED IN try BLOCK
#     print("Youy can't divide by zero!")
#
# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst Number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond Number: ")
    if second_number == 'q':
        break
    try:    # INCLUDES ONLY CODE THAT MIGHT CAUSE AN ERROR/EXCEPTION TO BE RAISED -> ANY CODE DEPENDING ON TRY BLOCK IS ADDED TO ELSE BLOCK
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:   # IF ERROR OCCURS
        print("You can't divide by zero!")
    else:   # ADDITIONAL CODE TO RUN IF TRY BLOCK IS SUCCESSFUL
        print(answer)
    break
