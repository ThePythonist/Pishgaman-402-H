# def is_prime(number):
#     divisors = [i for i in range(1, number + 1) if number % i == 0]  # Shomarande ha
#     print(divisors)
#     print("Prime") if len(divisors) == 2 else print("Composite")
#
#
# is_prime(int(input("Enter any number : ")))

# -----------------------------------------------------

def is_prime(number):
    divisors = [i for i in range(1, number + 1) if number % i == 0]  # Shomarande ha
    print(divisors)
    return "Prime" if len(divisors) == 2 else "Composite"


print(is_prime(int(input("Enter any number : "))))
