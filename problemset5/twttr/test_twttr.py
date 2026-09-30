from twttr import shorten


def main():
    test_lowercase()
    test_uppercase()
    test_punctuation()
    test_numbers()


def test_lowercase():
    assert shorten("aeiou") == ""
    assert shorten("twttr") == "twttr"

def test_uppercase():
    assert shorten("AEIOU") == ""
    assert shorten("TWTTR") == "TWTTR"

def test_punctuation():
    assert shorten("+=_-.") == "+=_-."
    assert shorten("twitter>X") == "twttr>X"

def test_numbers():
    assert shorten("0123456789") == "0123456789"
    assert shorten("cs50") == "cs50"


if __name__ == "__main__":
    main()