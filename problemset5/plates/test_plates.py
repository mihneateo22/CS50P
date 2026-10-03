from plates import is_valid
import string

def test_min2letters():
    assert is_valid("A2") == False
    assert is_valid("AA") == True

def test_len():
    assert is_valid("A") == False
    assert is_valid("2") == False
    assert is_valid("23") == False
    assert is_valid("OUTATIME") == False

def test_digits():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False
    assert is_valid("AAA202") == True
    assert is_valid("2222") == False

def test_punctuation():
    for character in string.punctuation:
        assert is_valid(f"P{character}I314") == False
    assert is_valid("P I314") == False