items = ["mouse", "keyboard", 4600, 7.5, True, 19, 0, "monitor"]
numbers = []

for i in items:
    # if type(i) == int or type(i) == float:
    if type(i) in [int, float]:
        numbers.append(i)

print(numbers)
