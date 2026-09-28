import random


def main():
    n = get_level()
    x = generate_integer(n)
    y = generate_integer(n)

    i = 10
    score = 0
    count = 0
    while i != 0:
        sumxy = x + y
        try:
            check_sum = int(input(f"{x} + {y} = "))
        except ValueError:
            check_sum = None

        if check_sum != sumxy:
            if count < 2:
                print("EEE")
                count += 1
                continue
            else: 
                print("EEE")
                print(f"{x} + {y} = {sumxy}")
        else:
            score += 1
        
        x = generate_integer(n)
        y = generate_integer(n)
        count = 0
        i -= 1
    
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue

        if level in [1, 2, 3]:
            return level


def generate_integer(level):

    if level not in [1, 2, 3]:
        raise ValueError("Not a valid level")

    if level == 1:
        inferior_limit = 0
        superior_limit = 9
    else:
        inferior_limit = 10 ** (level - 1)
        superior_limit = 10 ** level - 1
    
    number_generated = random.randint(inferior_limit, superior_limit)
    return number_generated


if __name__ == "__main__":
    main()