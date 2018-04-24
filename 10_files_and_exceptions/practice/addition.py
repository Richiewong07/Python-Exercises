# Write a program that prompts for two numbers. Add them together and print the result. Catch the TypeError if either input value is not a number, and print a friendly error message. Test your program by entering two numbers and then by entering some text instead of a number.


try:
    num_1 = int(input("Enter a number: "))
    num_2 = int(input("Enter another number: "))
except ValueError:
    print("One of your inputs was not a number. Please try again.")
    main()
else:
    sum = num_1 + num_2
    print('The sum of {} and {} is {}.'.format(num_1, num_2, sum))
