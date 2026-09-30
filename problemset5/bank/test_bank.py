from bank import value
import string

#added a test for hello something, otherwise the code would end up to be good for this too:
'''
if greeting == "hello":
    return 0
'''
#in this case(for the if statement above) 
'''assert value("hello example") == 0''' #would fail

def test_uppercase():
    assert value("HELLO") == 0
    assert value("HELLO MAN") == 0
    assert value("HI") == 20
    assert value("HOLA") == 20
    assert value("WASSUP") == 100

def test_lowercase():
    assert value("hello") == 0
    assert value("hello man") == 0
    assert value("hi") == 20
    assert value("hola") == 20
    assert value("wassup") == 100

def test_mixedcase():
    assert value("HelLo") == 0
    assert value("hEllo Man") == 0
    assert value("hI") == 20
    assert value("hOLa") == 20
    assert value("waSSup") == 100

def test_middle_h():
    assert value("aloha") == 100
    assert value("ALOHA") == 100

def test_numbers():
    assert value(string.digits) == 100

def test_punctuation():
    assert value(string.punctuation) == 100