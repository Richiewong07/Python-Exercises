# REPLACE PYTHON WITH THE NAME OF ANOTHER LANGUAGE

file_name = 'practice/learning_python.txt'

with open(file_name) as file_objects:
    lines = file_objects.readlines()

    for line in lines:
        line = line.replace('Python', 'Java').rstrip()
        print(line)
