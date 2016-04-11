
dictionary = {}
import sys

def add_word_to_dict(word):
    if word in dictionary:
        dictionary[word] += 1
    else:
        dictionary[word] = 1

def word_count(file):
    """Counts the number of times a word appears in a file"""
    with open(file) as file_in_use:
        
        # iterates through lines in file
        for line in file_in_use:
            # iterates through words in list line
            for word in line.split():
                word = word.lower() 
                # adds word to dictionary at count = 1, or ups the count
                # checks for punctuation 
                if word.isalpha():
                    add_word_to_dict(word) 
                else:
                    word = word[:-1]
                    add_word_to_dict(word)

    info = sorted(dictionary.items(), key= lambda x: x[1])

    print info


word_count(sys.argv[1])