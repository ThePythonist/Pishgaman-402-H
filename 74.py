# def divisors(x):
#     divs = [i for i in range(1, x + 1) if x % i == 0]
#     return divs
#
#
# m = map(divisors, [6, 10, 12])
# for i in m:
#     print(i)

# --------------------------------------------------------

m = map(lambda x: [i for i in range(1, x + 1)], [6, 12, 20])

for i in m:
    print(i)
