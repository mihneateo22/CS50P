import sys
import csv

def main():
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    except IndexError:
        sys.exit("Too few command-line arguments")
    new_csv(arg1, arg2)

def convert_name(full_name):
    return full_name.split(", ")

def new_csv(arg1, arg2):
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not (arg1.endswith(".csv") and arg2.endswith(".csv")):
        sys.exit("One of the input files is not a CSV file. Check again.")

    try:
        with open(arg1, "r") as infile:
            with open(arg2, "w", newline="") as outfile:
                reader = csv.reader(infile)
                writer = csv.writer(outfile)
                first_line = next(reader) # name, house
                writer.writerow(["first", "last", "house"])
                for element in reader:
                    last, first = convert_name(element[0])
                    writer.writerow([first, last, element[1]])
    except FileNotFoundError:
        sys.exit(f"Could not read {arg1}")

if __name__ == "__main__":
    main()