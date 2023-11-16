from random import randint

number = randint(0, 10)
chances = 5

print("Welcome to number guessing game")

while chances > 0:
    print(f"You have {chances} chances left")
    guess = int(input("Guess the number : "))
    chances -= 1

    if guess == number:
        print("You won!")
        break
    elif guess > number:
        print("Try smaller")
    else:
        print("Try bigger")
else:
    print(f"Game over! The number was {number}")
