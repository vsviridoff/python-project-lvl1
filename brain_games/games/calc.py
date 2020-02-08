from random import randint, choice
from operator import add, sub, mul

DESCRIPTION = 'What is the result of the expression?'


def logic_game():
    number_one = randint(1, 10)
    number_two = randint(1, 10)
    operators_list = [('+', add), ('-', sub), ('*', mul)]

    operator, function = choice(operators_list)

    correct_answer = function(number_one, number_two)
    result = str(correct_answer)

    expression = "{} {} {}".format(number_one, operator, number_two)

    return result, expression
