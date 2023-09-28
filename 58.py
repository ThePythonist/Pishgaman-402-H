# def adder(number):
#     n = 0
#     for i in str(number):
#         n += int(i)
#
#     print(n)
#
#
# adder(42452)

def adder(number):
    digits = []
    for i in str(number):
        digits.append(int(i))

    print(sum(digits))


adder(int(input("Enter any number : ")))
