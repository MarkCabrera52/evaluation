class Calculator:
    def eval(self, expression):

        # Remove white spaces
        expression = expression.replace(" ", "")

        # Check for '+'
        if expression.count("+") != 1:
            print("Invalid input: not a valid addition statement.")
            return None

        #retrive the operands
        operands = expression.split("+")

        #compute the addition
        try:
            num1 = float(operands[0])
            num2 = float(operands[1])
            result = num1 + num2
            return result
        except ValueError:
            print("One or both operands are not valid numbers.")
            return None

    def run(self):
        # Run until the user cancels, ctl + C
        while True:
            expression = input('Enter an infix addition statement: ')
            result = self.eval(expression)
            if result is not None:
                print(' = ', result)

if __name__ == "__main__":
    # If this file is run directly from the command line, run the calculator
    c = Calculator()
    c.run()
