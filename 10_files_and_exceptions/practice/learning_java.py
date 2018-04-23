# REPLACE PYTHON WITH THE NAME OF ANOTHER LANGUAGE

file_name = 'practice/learning_python.txt'

with open(file_name) as file_objects:
    for line in file_objects:
        print(line.replace('Python', 'Java').rstrip())
