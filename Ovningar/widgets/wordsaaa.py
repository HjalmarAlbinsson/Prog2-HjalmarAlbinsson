def load_words(new_validwords):
    with open("") as word_file:
        valid_words = word_file.readlines()

    with open("") as word_file:
        for line in valid_words:
            b = line.strip("\n").upper()
            if b in new_validwords:
                print(b)
                word_file.write(line)


def load_words2():
    yeah = set()
    with open("") as word_file:
        valid_words = set(word_file.read().split())
    for word in valid_words:
        if len(word) == 5:
            yeah.add(word.upper())

    return yeah


#y = load_words2()

#print(y)
#load_words(y)
