import sys
from tabulate import tabulate

def main():
    try:
        arg = sys.argv[1]
    except IndexError:
        sys.exit("Too few command-line arguments")
    
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    
    format_print(arg)


def format_print(arg):
    if not arg.endswith(".csv"):
        sys.exit("Not a CSV file")
    try:
        with open(arg, "r") as file:
            first_line = file.readline()
            headers = first_line.strip().split(",")

            rows = []

            for row in file:
                cells = row.strip().split(",")
                rows.append(cells)
            
            print(tabulate(rows, headers, tablefmt="grid"))
    except FileNotFoundError:
        sys.exit("File does not exist")

if __name__ == "__main__":
    main()