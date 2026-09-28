from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
list_of_fonts = figlet.getFonts()

if len(sys.argv) == 2 or len(sys.argv) > 3:
    sys.exit("Invalid usage")
elif sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid usage")
elif sys.argv[2] not in list_of_fonts:
    sys.exit("Invalid usage")

text = input("Input: ")

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(list_of_fonts))
elif len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])

print(figlet.renderText(text))