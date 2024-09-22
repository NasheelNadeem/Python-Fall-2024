def add(x, y):
    add= x+y
    return add

def subtract(x, y):
    subtract= x-y
    return subtract

def multiply(x, y):
    multiply= x*y
    return multiply

def divide(x, y):
    divide= x/y
    return divide

def main():
    num1=int(input("enter first number: "))
    num2= int(input("enter second number: "))
    addition=add(num1,num2)
    print("Addition:",addition)
    subtraction= subtract(num1, num2)
    print("subtraction:", subtraction)
    multiplication= multiply(num1, num2)
    print("Multiplication:", multiplication)
    division= divide(num1, num2)
    print("Division", division)

main()