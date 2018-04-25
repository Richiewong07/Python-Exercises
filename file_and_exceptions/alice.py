filename = "text_files/alice.txt"


try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + " does not exists."
    print(msg)
else:
    words = contents.split()    # SPLIT ALL THE WORDS IN FILE INTO A LIST
    num_words = len(words)      # GET LENGTH OF LIST
    print("The file " + filename + " has about " + str(num_words) + " words.")
