import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    list_of_ums = re.findall(r"\bum\b", s, flags=re.IGNORECASE)
    return len(list_of_ums)


if __name__ == "__main__":
    main()