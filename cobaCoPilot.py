# sum three numbers
def sum(a, b, c):
    return a + b + c
a, b, c = eval(input("Enter three numbers: "))
print("The sum of", a, ",", b, "and", c, "is", sum(a, b, c))