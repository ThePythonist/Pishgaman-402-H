n = int(input("How many numbers ? "))
numbers = []

for i in range(n):
    x = int(input("Enter any number : "))
    numbers.append(x)

print(max(numbers))
