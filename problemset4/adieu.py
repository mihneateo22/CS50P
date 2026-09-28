import inflect

p = inflect.engine()

list_of_names = []
song = "Adieu, adieu, to "
while True:
    try:
        name = input("Name: ")
        list_of_names.append(name)
    except EOFError:
        print()
        break
names = p.join(list_of_names)
print(song + names)