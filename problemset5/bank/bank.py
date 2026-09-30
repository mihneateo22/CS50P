def main():
    greeting = input("Input a greeting: ")
    print("Output:", value(greeting))


def value(greeting):
    #lstrip() is not necessary(mentioned in the problem statement), but why not?
    greeting = greeting.lower().lstrip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()