numbers = []

for i in range(3):
    x = input("Entry : ")

    try:
        x = int(x)
        numbers.append(x)
    except ValueError:
        pass

print(numbers)
