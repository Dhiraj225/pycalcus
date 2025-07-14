def calculator():
    print("Simple Calculator")
    num1 = float(input("Enter first number: "))
    op = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == '*':
        result = num1 * num2
    elif op == '/':
        if num2 == 0:
            print("Error: Division by zero!")
            return
        result = num1 / num2
    else:
        print("Invalid operator!")
        return

    print(f"{num1} {op} {num2} = {result}")

calculator()
