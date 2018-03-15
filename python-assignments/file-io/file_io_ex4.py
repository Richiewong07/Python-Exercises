# Write program that takes a JSON file name as input and plots the X,Y data. Exchange JSON data with others to test your program more thoroughly.
#
# Example Format:
#
# {
#   "data": [
#     [1, 1],
#     [2, 2],
#     [3, 3],
#     [4, 4]
#   ]
# }

from matplotlib import pyplot

# def plot(contents):
#     x = contents[test]
#     print(x)


def main():
    file_name = input("Enter a file name here: ")   # test4.txt
    file_handle = open(file_name , 'r')
    contents = file_handle.read()
    file_handle.close()
    print(contents)
    print(conte)


if __name__ == '__main__':
    main()
