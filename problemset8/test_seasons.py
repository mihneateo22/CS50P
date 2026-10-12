from seasons import minutes_in_words
from datetime import date

def test_minutes():
    assert minutes_in_words(date(2025, 10, 12), date(2026, 10, 12)) == "Five hundred twenty-five thousand, six hundred minutes"
    assert minutes_in_words(date(2024, 10, 12), date(2026, 10, 12)) == "One million, fifty-one thousand, two hundred minutes"
    assert minutes_in_words(date(2023, 10, 12), date(2024, 10, 12)) == "Five hundred twenty-seven thousand forty minutes"
    assert minutes_in_words(date(2026, 10, 12), date(2026, 10, 12)) == "Zero minutes"
