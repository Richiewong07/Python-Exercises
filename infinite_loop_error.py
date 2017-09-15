while True:
  try:
    x = int(input("Please enter a number: "))
    break
  except ValueError:
    print("Oops!  That was no valid number.  Try again...")

finally:
    always_execute('always execute')

# except Value Error catches the error
# do not want to catch all error
# better to use except with error you are catching
