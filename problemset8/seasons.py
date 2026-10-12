from datetime import date, timedelta
import inflect
import re
import sys

def main():
    my_birthday = input("Date of birth: ")
    if matches := re.search(r"^([0-9]{4})-(0[1-9]|1[0-2])-(0[1-9]|1[0-9]|2[0-9]|3[0-1])$", my_birthday):
        try:
            d = date.fromisoformat(my_birthday)
        except ValueError:
            sys.exit("Invalid date")
        if d > date.today() :
            sys.exit("Invalid date")
        #print(matches.groups())
        print(minutes_in_words(d, date.today()))
    else:
        sys.exit("Invalid date")


def minutes_in_words(birth, today):
    days = (today - birth).days
    minutes = days * 60 * 24
    p = inflect.engine()
    words = p.number_to_words(minutes, andword="")
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()