word = "python"
d = {}
# --------------------------------
# n = 0
# for i in word:
#     d.setdefault(n, i)
#     n += 1
#
# print(d)
# --------------------------------
# for i in range(len(word)):
#     d.setdefault(i, word[i])
#
# print(d)
# --------------------------------
indexes = range(len(word))
d = zip(indexes, word)
print(dict(d))
