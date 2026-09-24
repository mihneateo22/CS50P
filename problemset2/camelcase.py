camelCase = input("camelCase: ")
print("snake_case: ", end="")

for character in camelCase:
    if character.isupper():
        character = character.lower()
        print('_', end="")
    print(character, end="")
print()