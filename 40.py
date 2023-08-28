# numbers = [14, 21, 6, 19, 23, 10]
# numbers.sort()
# print(numbers[::-1])

numbers = []
for i in range(4):
    x = int(input("Enter any number : "))
    numbers.append(x)

numbers.sort(reverse=True)
print(numbers)
