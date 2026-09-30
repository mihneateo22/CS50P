def main():
    word = input("Input a string: ")
    print("Output:", shorten(word))


def shorten(word):
    no_vowel = ""
    vowels = "aeiouAEIOU"
    for character in word:
        if character not in vowels:
            no_vowel += character
    return no_vowel


if __name__ == "__main__":
    main()