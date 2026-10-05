from numb3rs import validate


def test_valid():
    assert validate("127.0.0.1") == True
    assert validate("255.255.255.255") == True
    assert validate("0.0.0.0") == True

def test_out_of_range():
    assert validate("256.0.0.1") == False
    assert validate("0.256.0.1") == False
    assert validate("0.0.256.1") == False
    assert validate("1.0.0.256") == False
    assert validate("256.512.999.257") == False

def test_format():
    assert validate("cat") == False
    assert validate("") == False
    assert validate("1.2.3.4.5") == False
    assert validate("1.2.3") == False
    assert validate("1.2.3.+4") == False
    assert validate("1.2..3.4") == False
    assert validate("1.2.  4.5") == False
    assert validate("1.2.3. ") == False
    assert validate("1.2|3.4") == False

def test_leading_zeros():
    assert validate("001.168.0.1") == False
    assert validate("192.01.1.1") == False
    assert validate("192.168.001.1") == False
    assert validate("192.168.0.001") == False
    assert validate("10.0.0.100") == True