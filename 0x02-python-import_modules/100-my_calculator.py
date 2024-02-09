#!/usr/bin/python3
import sys

def calculate(a, operator, b):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b != 0:
            return a / b
        else:
            print("Error: Division by zero")
            sys.exit(1)
    else:
        print(f"Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    operator = sys.argv[2]
    b = int(sys.argv[3])

    result = calculate(a, operator, b)

    print(f"{a} {operator} {b} = {result}")

if __name__ == "__main__":
    main()
