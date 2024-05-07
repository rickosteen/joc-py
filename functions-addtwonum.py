#functions - Writing Functions - add two numbers
def add():
    num1 = eval(input("type a number to add: "))
    num2 = eval(input("type second number to add: "))
    sum = num1 + num2
    print("The sum of num1 and num2 = ", sum)
    return num1, num2
def multiply(num1,num2):
    product = num1 * num2
    print("The product of num1*num2 is: ", product)
def main():
    num1, num2, = add()
    multiply(num1,num2)
main()
