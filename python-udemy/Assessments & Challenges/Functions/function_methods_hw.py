# Write a function that computes the volume of a sphere given its radius.

def vol(rad):
    pi = 3.14
    print ((4/3) * pi * (rad ** 3))

results = vol(2)


# Write a function that checks whether a number is in a given range (inclusive of high and low)

def ran_check(num, low, high):
    if num in range(low, high):
        print ("%s is in the range" %str(num))
    else:
        print ("The number is outside the range")

ran_check(5, 1, 10)


# If you only wanted to return a boolean:

def ran_bool(num, low, high):
    return num in range(low, high)

results = ran_bool(3, 1, 10)

print(results)


# Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.

def up_low(string):
    dict = {"upper": 0, "lower": 0}
    for char in string:
        if char.isupper():
            dict["upper"] += 1
        elif char.islower():
            dict["lower"] += 1
        else:
            pass
    print("Original String: ", string)
    print("# of Uppercase Characters: ", dict["upper"])
    print("# of Lowercase Characters: ", dict["lower"])

string = "Hello World. My Name is Richie Wong."

up_low(string)


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    print(x)

unique_list([1, 1, 1, 2, 3, 4, 4, 5, 6])


# Write a Python function to multiply all the numbers in a list.

def multiply(nums):
    total = nums[0]
    for x in nums:
        total *= x
    return total

results = multiply([1, 2, 3, 4])
print(results)

# Write a Python function that checks whether a passed string is palindrome or not.

def palidrome(s):
    return s == s[::1]

print(palidrome('helleh'))


# Write a Python function to check whether a string is pangram or not.
