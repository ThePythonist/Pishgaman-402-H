numbers = []

for i in range(3):
    x = input("Entry : ")

    try:
        x = float(x)
        if str(x)[-2:] == ".0":
            numbers.append(int(x))
        else:
            numbers.append(x)
    except ValueError:
        pass

print(numbers)
