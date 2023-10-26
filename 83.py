# f = open("words.txt").readlines()
# five_letters = []
#
# for i in f:
#     if len(i) == 6:
#         five_letters.append(i)
#
# open("fiveletters.txt", "w").writelines(five_letters)
# print("Done")

# -----------------------------------------------------------

f = open("words.txt").readlines()
five_letters = []

for i in f:
    if len(i) == 6:
        five_letters.append(i)

output = "".join(five_letters)
open("fiveletters.txt", "w").write(output)
