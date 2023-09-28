def revsort(numbers):
    # items.sort()
    # items = list(reversed(items))
    # print(items)

    numbers.sort()
    print(numbers[::-1])


numbers = [15, 10, 25, 5, 30]
revsort(numbers)
