from add_sub import addition, subtraction
from mul_div import multiplication, quotient

n1 = int(input("enter a number1: "))
n2 = int(input("enter a number2: "))

choice = int(input("Enter your choice: "))
match choice:
    case 1:
        S = addition(n1, n2)
        print(S)
    case 2:
        Sub = subtraction(n1, n2)
        print(Sub)
    case 3:
        mult = multiplication(n1, n2)
        print(mult)
    case 4:
        div = quotient(n1, n2)
        print(div)
    case _:
        print("Enter a Vaild choice")
