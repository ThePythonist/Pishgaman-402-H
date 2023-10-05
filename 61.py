def check(word):
    if len(word) == len(set(word)):
        print(False)
    else:
        print(True)


check("aria")
