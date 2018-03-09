# Prompt the user for a number in degrees Celsius, and convert the value to
# degrees in Fahrenheit and display it to the user.

temperature_in_c = int(input('Temperature in C?'))
temperature_in_f = str(temperature_in_c * 1.8 + 32)
print (temperature_in_f + ' F')
