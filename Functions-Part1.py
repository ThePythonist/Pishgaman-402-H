# def checknumber(x):
#     if type(x) in [int, float]:
#         # print("Okay continue")
#         return "Number"
#     else:
#         # print("Not okay")
#         return "Not Number"


# print(checknumber("x"))

# if checknumber("X") == "Number":
#     print("Yes")
# else:
#     print("No")

# -------------------------------------------

def checknumber(x):
    if x % 2 == 0:
        print(x,"Even")
        # return "Even"
    else:
        print(x,"Odd")
        # return "Odd"


# checknumber(7)
# print(checknumber(14))


numbers = [11, 4, 2, 3, 5, 12, 16]

for i in numbers:
    checknumber(i)
