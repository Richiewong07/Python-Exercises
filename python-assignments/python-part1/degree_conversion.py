# Prompt the user for a number in degrees Celsius, and convert the value to
# degrees in Fahrenheit and display it to the user.

input = int(input('Enter a Temperature in Celsius: '))

def degree_conv(temp_c):
    temp_f = input * 1.8 + 32
    print('{} degrees in Celsius is {} degrees in Fahrenheit'.format(temp_c, temp_f))

degree_conv(input)
