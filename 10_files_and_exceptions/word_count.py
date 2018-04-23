def count_words(filename):
    """COUNT THE APPROXIMATE NUMBER OF WORDS IN A FILE."""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        # msg = "Sorry, the file " + filename + " does not exists."
        # print(msg)
        pass
    else:
        words = contents.split()    # SPLIT ALL THE WORDS IN FILE INTO A LIST
        num_words = len(words)      # GET LENGTH OF LIST
        print("The file " + filename + " has about " + str(num_words) + " words.")


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']


for filename in filenames:
    count_words(filename)
