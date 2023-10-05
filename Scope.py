# balance = 1500  # Global
#
#
# def check_balance():
#     print(balance)
#
# check_balance()

# ---------------------------------

# def check_balance():
#     balance = 1200  # Local
#     # print(balance)
#
#
# check_balance()

# ---------------------------------

balance = 0


def change_balance(money):
    global balance
    balance += money


print(balance)
change_balance(500)
print(balance)
change_balance(-100)
print(balance)

# ---------------------------------
x = 7


def func():
    x = 10
    print(x)


print(x)
