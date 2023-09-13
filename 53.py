info = {
    "classname": "pishgaman h",
    "students": ["sepehr", "yosef", "ilia", "arian"],
    "teacher": "sadeghi",
    "ages": {
        "arian": 14,
        "sepehr": 14,
        "ilia": 14,
        "yosef": 16,
    }
}

key = input("Enter key to search : ")

if key in info:
    print("Found :", info[key])
else:
    print("Not Found")

# d = info["ages"]
# print(d["arian"])
