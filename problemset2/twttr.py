text = input("Input: ")
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
print("Output: ", end="")
for character in text:
    if character not in vowels:
        print(character, end="")
print()
