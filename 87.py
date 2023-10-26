# lines = open("words.txt").readlines()
# words = []
#
# for i in lines:
#     words.append(i[:-1])
#
# print(words)


lines = open("words.txt").read().split("\n")
print(lines)
