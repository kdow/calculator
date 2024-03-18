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
        return num1 / num2


def main() -> None:
    calculator = Calculator()

    print(calculator.state)

    run_program = True

    while run_program:
        user_input = input('>')
        parse_input = list(user_input)

        for char in parse_input:
            if char == 'q':
                run_program = False


if __name__ == '__main__':
    exit(main())