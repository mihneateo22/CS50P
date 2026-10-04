import sys, os
from PIL import Image, ImageOps


def main():
    try:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
    except IndexError:
        sys.exit("Too few command-line arguments")
    extensions = (".jpg", ".jpeg", ".png")
    ext_arg1 = os.path.splitext(arg1)[1].lower()
    ext_arg2 = os.path.splitext(arg2)[1].lower()

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif ext_arg1 not in extensions:
        sys.exit("Invalid input")
    elif ext_arg2 not in extensions:
        sys.exit("Invalid output")
    elif ext_arg1 != ext_arg2:
        sys.exit("Input and output have different extensions")
    try_on(arg1, arg2)


def try_on(arg1, arg2):
    try:
        photo = Image.open(arg1)    
    except FileNotFoundError:
        sys.exit("Image not found")
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(arg2)


if __name__ == "__main__":
    main()