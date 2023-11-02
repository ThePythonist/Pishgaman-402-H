lines = open("words.txt").read().split("\n")

numbers = []
# sdfg3sf1

for i in lines:
    if not i.isdigit():
        for j in i:
            if j.isdigit():
                numbers.append(i)
                break  # for j ra break mikonad

print(numbers)
