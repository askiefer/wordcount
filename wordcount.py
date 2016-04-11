
def word_count(file):
    """"""
    with open(file) as file_in_use:
        dictionary = {}
        # iterates through lines in file
        for line in file_in_use:
            # iterates through words in list line
            for word in line.split():
                # adds word to dictionary at count = 1, or ups the count
                if word in dictionary:
                        dictionary[word] += 1
                else:
                    dictionary[word] = 1
    print dictionary

word_count("test.txt")