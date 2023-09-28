def is_perfect(number):
    divs = [i for i in range(1, number) if number % i == 0]
    if sum(divs) == number:
        print(True)
    else :
        print(False)


is_perfect(int(input("Enter any number : ")))
