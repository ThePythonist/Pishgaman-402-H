num = int(input("Enter any number : "))
divs = [i for i in range(1, num) if num % i == 0]
print((lambda num: True if sum(divs) == num else False)(num))
