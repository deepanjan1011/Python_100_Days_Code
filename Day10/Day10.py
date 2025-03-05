def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

option_dict = {"+": add, "-": subtract, "*": multiply, "/": divide}
import art
print(art.logo)
f_no = int(input("What's the first number?: "))
