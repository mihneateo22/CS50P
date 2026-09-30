import string

def main():
    s = input("Plate: ")
    if is_valid(s):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False
    if not (s[0:2].isalpha() and s[0:2].isupper()):
        return False
    if not s.isalnum():
        return False
    
    digits_flag = False
    for character in s[2:]:
        if character in string.digits:
            if character == '0' and not digits_flag:
                return False
            digits_flag = True
        elif character in string.ascii_uppercase and digits_flag:
            return False
    return True


if __name__ == "__main__":
    main()