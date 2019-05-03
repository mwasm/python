
def add(num1, num2):
    """Returns num1 plus num2"""
    return num1 + num2


def sub(num1, num2):
    """Returns num1 minus num2"""
    return num1 - num2


def mul(num1, num2):
    """Returns num1 multiply num2"""
    return num1 * num2


def div(num1, num2):
    """Returns num1 divide num2"""
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("You can't divide by Zero!")
        return 0


def run_operations(operation, num1, num2):
    """"Run the operation according to the inputs passed."""
    if operation == 1:
        print(add(num1, num2))
    elif operation == 2:
        print(sub(num1, num2))
    elif operation == 3:
        print(mul(num1, num2))
    elif operation == 4:
        print(div(num1, num2))
    else:
        print('Please follow the instructions.')


def main():
    user_continue = True
    while user_continue:
        valid_input = False
        while not valid_input:
            try:
                num1 = int(input('Enter the num1:'))
                num2 = int(input('Enter the num2:'))
                operation = int(input('What operation do you want to perform? 1) Add, 2) Sub, 3) Mul, or 4) '
                                      'Div. Enter number.'))
                valid_input = True
            except ValueError:
                print('Invalid input. Try again.')
            else:
                run_operations(operation, num1, num2)
        # Ask user to continue.
        user_yn = input("Would you like to run another calculation? (y/n)")
        if user_yn != 'y':
            user_continue = False


main()