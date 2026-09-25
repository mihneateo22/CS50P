import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0] not in string.ascii_uppercase or s[1] not in string.ascii_uppercase:
        return False
    if s.isalnum() == False:
        return False
    else:
        count_digits = 0
        for character in s[2:]:
            if character == '0' and count_digits == 0:
                return False
            elif character in string.digits:
                count_digits = count_digits + 1
            if character in string.ascii_uppercase and count_digits != 0:
                return False
    return True

main()