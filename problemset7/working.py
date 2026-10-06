import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.search(r"^(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (PM|AM)$", s):
        start = to_24(matches.group(1), matches.group(2), matches.group(3))
        end = to_24(matches.group(4), matches.group(5), matches.group(6))
        return f"{start} to {end}"
    else:   
        raise ValueError


def to_24(hour, minute, meridiem):
    if minute is None:
        minute = "00"
    hour = int(hour)
    if hour == 12:
        if meridiem == "AM":
            hour = 0
    elif meridiem == "PM":
        hour += 12

    return f"{hour:02}:{minute}"
    

if __name__ == "__main__":
    main()