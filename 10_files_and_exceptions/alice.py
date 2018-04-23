filename = "alice.txt"

try:
    with open(filename) as f_objects:
        contents = f_objects.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exists."
    print(msg)
