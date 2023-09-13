scores = {
    "riazi": 17,
    "olom": 20,
    "ejtemaei": 14,
    "farsi": 12,
    "arabi": 7,
    "zaban": 19
}

for k, v in scores.items():
    if v >= 10:
        print(k, ": Passed")
    else:
        print(k, ": Failed")

# SUM = 0
# TEDAD = 0
# for i in scores.values():
#     SUM += i
#     TEDAD += 1
#
# print(SUM/TEDAD)

average = sum(scores.values()) / len(scores)
print(average)
