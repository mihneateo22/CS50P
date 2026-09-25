while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split('/')
        x = int(x)
        y = int(y)

        if x < 0:
            raise ValueError

        if x > y:
            print("The tank can not be more than FULL. Try again!")
            continue
        
        result = x / y * 100

    except ValueError:
        print("Something went wrong. Try again!")
    except ZeroDivisionError:
        print("You can not divide by 0. Try again!")
    else:
        break

if result <= 1:
    print("E")
elif result >= 99:
    print("F")
else:
    print(f"{result:.0f}%")
