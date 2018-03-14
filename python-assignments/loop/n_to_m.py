# 2. n to m
# Same as the previous problem, except you will prompt the user for the number to start on and the number to end on. Example session:
#
# $ python n_to_m.py
# Start from: 2
# End on: 8
# 2
# 3
# 4
# 5
# 6
# 7
# 8

start_num = int(input('Start from:'))
end_num = int(input('End on:'))

def counter(start, end):
    for num in range(start, end + 1):
        print(num)

counter(start_num, end_num)
