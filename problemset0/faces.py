def main():
    text = input("Please type some input here so i can call the \"convert(str)\" function : ")
    print(convert(text))

def convert(word):
    return word.replace(":)", "🙂").replace(":(", "🙁")

main()