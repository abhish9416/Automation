import random

num = random.randint(1,10)

guess = 0

while guess != num:
    guess = int(input("Guess the Number : "))

    if guess > num:
        print("It is larger")
    elif guess < num:
        print("It is Smaller")
    else:
        print("Number Found")

