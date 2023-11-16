from random import randint, choice, sample


def generate1(length):
    password = []

    for i in range(length):
        digit = str(randint(0, 9))
        password.append(digit)

    output = "".join(password)
    print(output)


def generate2(length):
    password = []

    for i in range(length):
        digit = str(choice(range(0, 10)))
        password.append(digit)

    output = "".join(password)
    print(output)


def generate3(length):
    password = [str(i) for i in sample(range(0, 10), length)]
    output = "".join(password)
    print(output)


generate3(6)
