import sys

def main():
    try:
        argument = sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    print(count_lines(argument))

def count_lines(argument):
    if not argument.endswith(".py"):
        sys.exit("Not a Python file")

    try:
        with open(argument, "r") as file:
            count = 0
            for line in file:
                if not (line.lstrip() == "" or line.lstrip().startswith("#")):
                    count += 1
        return count
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()