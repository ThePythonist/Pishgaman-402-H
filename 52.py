numbers = []
x = ""
while x != "exit":
    x = input("Type something : ")
    try:
        x = float(x)
        if x == int(x):
            numbers.append(int(x))
        else:
            numbers.append(x)
    except ValueError:
        pass

print(numbers)
print(max(numbers))
