def find_longest1(text):
    text = text.split()
    lengths = []

    for i in text:
        lengths.append(len(i))

    longest = max(lengths)

    for word in text:
        if len(word) == longest:
            print(word)


def find_longest2(text):
    text = text.split()
    print(max(text, key=len))


def find_longest3(text):
    text = text.split()
    text.sort(key=len)
    print(text[-1])


find_longest1("Python is a good programming language")
find_longest2("Python is a good programming language")
find_longest3("Python is a good programming language")
