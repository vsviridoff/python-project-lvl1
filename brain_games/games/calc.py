from random import randint, choice

description = 'What is the result of the expression?'


def logic_game():
    number_one = randint(1, 10)
    number_two = randint(1, 10)
    operator = choice('+-*')

    if operator == '+':
        result = str(number_one + number_two)
    elif operator == '-':
        result = str(number_one - number_two)
    else:
        result = str(number_one * number_two)

    expression = str(number_one) + " {} ".format(operator) + str(number_two)

    return result, expression
