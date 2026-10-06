from validator_collection import validators, errors

def main():
    print(mail_validator(input("What's your email address? ")))


def mail_validator(s):
    try:
        validators.email(s)
    except errors.EmptyValueError:
        return "Invalid"
    except errors.InvalidEmailError:
        return "Invalid"
    return "Valid"


if __name__ == "__main__":
    main()