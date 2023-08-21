flag = 1

while flag:
    entry = input("Type something : ")
    if entry == "exit":
        flag = 0
        # break
    print(entry)
else:
    print("The flag has turned into False")
