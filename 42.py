# pythons = ["ilia", "sepehr", "arian", "yosef"]
# javas = ["yosef", "sepehr", "sina", "ali"]
# common = []
#
# for student in pythons:
#     if student in javas:
#         # common.append(student)
#         common += [student]
#
# print(common)


pythons = ["ilia", "sepehr", "arian", "yosef"]
javas = ["yosef", "sepehr", "sina", "ali"]
common = []

for i in pythons:  # Martabe ejrayi : i * j = 16
    for j in javas:
        if i == j:
            common.append(i)

print(common)
