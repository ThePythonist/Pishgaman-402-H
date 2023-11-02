lines = open("words.txt").read().split("\n")
print(lines)

open("onelinewords.txt", "w").writelines(lines)
