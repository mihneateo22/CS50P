import sys

exp = input("Expression: ")
x,y,z = exp.split()

#transforming x and z from strings to integers
x = int(x)
z = int(z)

result = 0

match y:
    case "+":
        result = x + z
    case "-":
        result = x - z
    case "*":
        result = x * z
    case "/":
        if z == 0:
            print("Error, you can not divide a number to 0!")
            sys.exit()
        else:
            result = x / z
print(f"{result:.1f}")

