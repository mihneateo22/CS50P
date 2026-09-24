exp = input("Expression: ")
x,y,z = exp.split()

#transforming x and z from strings to integers
x = int(x)
z = int(z)

match y:
    case "+":
        print(f"ANSWER : {float(x + z)}")
    case "-":
        print(f"ANSWER : {float(x - z)}")
    case "*":
        print(f"ANSWER : {float(x * z)}")
    case "/":
        if z == 0:
            print("Error, you can not divide a number to 0!")
        else:
            print(f"ANSWER : {float(x / z)}")

