import re, sys

def main():
    print(validate(input("IPv4 Address: ")))

    
def validate(ip):
    if matches := re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip):
        for number in matches.groups():
            if len(number) > 1 and number[0] == '0':
                return False
            elif not (0 <= int(number) <= 255):
                return False
    else:
        return False
    return True


if __name__ == "__main__":
    main()