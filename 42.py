pythons = ["ilia", "sepehr", "arian", "yosef"]
javas = ["yosef", "sepehr", "sina", "ali"]
common = []

for student in pythons:
    if student in javas:
        # common.append(student)
        common += [student]

print(common)
