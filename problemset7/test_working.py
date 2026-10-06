import pytest
from working import convert

def test_12():
    assert convert("12:00 AM to 12:00 PM") == "00:00 to 12:00"
    assert convert("12:00 PM to 12:00 AM") == "12:00 to 00:00"

def test_no_minutes_typed():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("11 AM to 7 PM") == "11:00 to 19:00"

def test_PMtoAM():
    assert convert("10 PM to 8 AM") == "22:00 to 08:00"

def test_input():
    with pytest.raises(ValueError):
        convert("9:60 AM to 5 PM")
    with pytest.raises(ValueError):
        convert("13 PM to 5 PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("8:00 am to 5:00 pm")