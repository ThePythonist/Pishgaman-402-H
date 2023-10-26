lines = open("words.txt").readlines()


def extract1(file):
    lengths = []
    for i in file:
        lengths.append(len(i))

    maxlen = max(lengths)

    for i in lines:
        if len(i) == maxlen:
            print(i)


def extract2(file):
    lengths = []
    for i in file:
        lengths.append(len(i))

    minlen = min(lengths)

    for i in lines:
        if len(i) == minlen:
            print(i)


extract1(lines)
extract2(lines)
