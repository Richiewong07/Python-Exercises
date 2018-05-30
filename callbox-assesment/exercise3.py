# Exercise​ ​3:

# Write​ ​a​ ​function​ ​that​ ​identifies​ ​if​ ​an​ ​integer​ ​is​ ​a​ ​power​ ​of​ ​2.​ ​The​ ​function​ ​should​ ​return​ ​a​ ​boolean. Explain​ ​why​ ​your​ ​function​ ​will​ ​work​ ​for​ ​any​ ​integer​ ​inputs​ ​that​ ​it​ ​receives.

# Examples:
# is_power_two(6)​ ​→​ ​false is_power_two(16)​ ​→​ ​true


input_num = 16

def is_power_two(num):
    """If a number is a power of 2 then the square root of the number must be a whole number. My function takes the square root of a input number and then checks if the square root of that number is an interger; return a boolean value."""

    square_root = num ** 0.5
    print(square_root.is_integer())


is_power_two(6)
is_power_two(16)
