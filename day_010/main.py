from art import logo

def calculator(num1, op, num2):
    if op == '+':
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        return num1 / num2

print(logo)

start = True

while start:
    new_calc = "y"

    first_num = float(input("What is the first number? "))
    while new_calc == "y":
        operator = input("+\n-\n*\n/\nPick an operation ")
        second_num = float(input("What is the second number? "))

        final = calculator(first_num, operator, second_num)

        print(f"{first_num} {operator} {second_num} = {final}")
        new_calc = input(f"Press 'y' to continue with {final} as your first number, or press 'n' to start a new calculator. ").lower()
        first_num = final