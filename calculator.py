from typing import Final

OPERATIONS: Final = ['+', '-', '*', '/']


class Calculator:
    def __init__(self):
        self.state = 0

    @staticmethod
    def add(num1: float, num2: float) -> float:
        return num1 + num2

    @staticmethod
    def subtract(num1: float, num2: float) -> float:
        return num1 - num2

    @staticmethod
    def multiply(num1: float, num2: float) -> float:
        return num1 * num2

    @staticmethod
    def divide(num1: float, num2: float) -> float:
        if num1 == 0 or num2 == 0:
            print('Cannot divide by zero')
            return 0.0
        return num1 / num2


def __handle_sign_change(num: str) -> str:
    if num[0] == '!':
        return str(float(num[1:]) * -1)
    else:
        return num


def __format(num: int | float) -> int | float:
    return int(num) if num.is_integer() else num


def main() -> None:
    calculator = Calculator()

    operation_map = {
        '+': calculator.add,
        '-': calculator.subtract,
        '*': calculator.multiply,
        '/': calculator.divide
    }

    print(calculator.state)

    run_program = True
    current_operation = num1 = num2 = None

    while run_program:
        user_input = input('>')
        parse_input = list(user_input)

        for char in parse_input:
            if char == 'q':
                run_program = False
            elif char == 'c':
                num1 = num2 = calculator.state = 0
                current_operation = None
            elif char == '=':
                result = operation_map[current_operation](
                    float(num1), 
                    float(num2)
                )
                num1 = calculator.state = __format(result)
                current_operation = num2 = None
            elif char in OPERATIONS:
                if current_operation:
                    result = operation_map[current_operation](
                        float(num1), 
                        float(num2)
                    )
                    num1 = calculator.state = __format(result)
                    num2 = None
                current_operation = char
            elif not num1:
                calculator.state = num1 = char
            elif not current_operation:
                num1 = str(num1) + char
                num1 = __handle_sign_change(num1)
                calculator.state = num1
            elif not num2:
                calculator.state = num2 = char
            else:
                num2 = str(num2) + char
                num2 = __handle_sign_change(num2)
                calculator.state = num2

        print(calculator.state)


if __name__ == '__main__':
    exit(main())