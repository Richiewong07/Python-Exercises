# Exercise​ ​1:

# Create​ ​a​ ​function​ ​that​ ​accepts​ ​a​ ​single​ ​array​ ​as​ ​an​ ​argument.​ ​Given​ ​an​ ​array​ ​of​ ​integers,​ ​x,​ ​sort x​ ​and​ ​split​ ​the​ ​integers​ ​into​ ​three​ ​smaller​ ​arrays​ ​of​ ​equal​ ​length.​ ​If​ ​the​ ​length​ ​of​ ​x​ ​is​ ​not​ ​evenly divisible​ ​by​ ​three,​ ​increase​ ​the​ ​size​ ​of​ ​the​ ​smaller​ ​arrays​ ​by​ ​one​ ​starting​ ​from​ ​the​ ​first​ ​array.​ ​The function​ ​should​ ​return​ ​an​ ​array​ ​of​ ​arrays.

# Example:
# Input​ ​=​ ​[2,1,3,4,7,5,9,6,8,13,12,11,10,0,15,16,14]
# Output​ ​=​ ​[​ ​[0,​ ​1,​ ​2,​ ​3,​ ​4,​ ​5],​ ​[6,​ ​7,​ ​8,​ ​9,​ ​10,​ ​11],​ ​[12,​ ​13,​ ​14,​ ​15,​ ​16]​ ​]



input = [2,1,3,4,7,5,9,6,8,13,12,11,10,0,15,16,14]


def split(array):
    """Function sorts and splits array into smaller subarrays then appends subarrays into single array"""

    split_array = []
    num = 3

    array.sort()
    size = int(round(len(array)/num))

    for i in range(0, len(array), size):
        split_array.append(array[i:i + size])
    return split_array

output = split(input)
print("Output = " + str(output))
