#simple python calculator
import math
operator = input("Enter an operator ( + , - , * , / , % , ^ ,)\n")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
if operator == "+":
    print(round(num1+num2,4))
elif operator == "-":
    print(round(num1-num2,4))
elif operator == "*":
    print(round(num1*num2,4))
elif operator == "/":
    print(round(num1/num2,4))
elif operator == "%":
    print(round(num1%num2,4))
elif operator == "^":
    print(round(math.pow(num1,num2),4))
else:
    print(f"\"{operator}\" is not a valid operator")