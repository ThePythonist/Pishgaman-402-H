items = ["mouse", "keyboard", 4600, 7.5, True, 19, 0, "monitor"]
words = []

for i in items:
    if type(i) == str:
        words.append(i)

print(words)
