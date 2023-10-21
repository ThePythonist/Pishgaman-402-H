f = open("words.txt").readlines()
five_letters = []

for i in f:
    if len(i) == 6:
        five_letters.append(i)

print(five_letters)
