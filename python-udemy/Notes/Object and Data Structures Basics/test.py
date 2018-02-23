# myfile = open('/Users/richiewong/Documents/Python-Exercises/python-udemy/test.txt')
#
# print(myfile.read())
#
# myfile.seek(0)
#
# print(myfile.readline())

# myfile.close()



# with open('test.txt', mode='r') as my_test_file:
#     contents = my_test_file.read()
#     print(contents)



with open('test.txt', mode='a') as f:
    f.write('FOUR ON FOURTH')

with open('test.txt', mode='r') as f:
    print(f.read())
