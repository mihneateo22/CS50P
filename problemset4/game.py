import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue

    if level > 0:
        break


random_number = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue

    if guess <= 0:
        continue
    elif guess < random_number:
        print("Too small!")
    elif guess > random_number:
        print("Too large!")
    else:
        print("Just right!")
        break