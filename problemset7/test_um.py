from um import count


def test_um_in_word():
    assert count("yummy") == 0
    assert count("hi. um, thanks for the album.") == 1

def test_ignore_case():
    assert count("Um") == 1
    assert count("uM") == 1
    assert count("UM") == 1

def test_begin_end_of_phrase():
    assert count("Um, how are you, um") == 2

def test_end_of_word():
    assert count("um?") == 1
    assert count("um...") == 1
    assert count("Um, thanks, um...") == 2