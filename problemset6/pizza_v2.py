import sys
import csv
from tabulate import tabulate


def main():
    try:
        arg = sys.argv[1]
    except IndexError:
        sys.exit("Too few command line arguments")
    print(format_print(arg))
    

def format_print(arg):
    if len(sys.argv) > 2:
        sys.exit("Too many command line arguments")
    elif not arg.endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(arg, "r") as file:
            reader = csv.reader(file)
            headers = next(reader) # the first line in the file in a list form []
            rows = list(reader) # a list of list. each list in the big list(rows) is a line in the file
            return tabulate(rows, headers, tablefmt="grid")
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()