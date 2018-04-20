file_name = 'text_files/learning_python.txt'


# PRINT CONTENT ONCE BY READING ENTIRE FILE
with open(file_name) as file_objects:
    contents = file_objects.read()
    print(contents.rstrip())

# PRINT ONCE BY LOOPING OVER THE FILE file_object
with open(file_name) as file_objects:
    for line in file_objects:
        print(line.rstrip())

# PRINT ONCE BY STORING THE LINES IN A LIST THEN WORKING THEM OUTSIDE THE WITH BLOCK
with open(file_name) as file_objects:
    lines = file_objects.readlines()

for line in lines:
    print(line.rstrip())

# REPLACE PYTHON WITH THE NAME OF ANOTHER LANGUAGE
with open(file_name) as file_objects:
    for line in file_objects:
        print(line.replace('Python', 'Java').rstrip())
