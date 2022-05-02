def print_upper_words(words, starts_with):
    """The function prints in uppercase all provided words that start with a letter
       that is in a given set of letter.
    """    
    for word in words:
        for char in starts_with:
            if char.upper() in word.upper():
                print(word.upper())
                break

print_upper_words(["first", "second", "third"], {"f", "T"})

    