from random import randint

description = 'Answer "yes" if number even otherwise answer "no".'


def logic_game():
    random_number = randint(1, 99)

    if random_number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'

    expression = '{}'.format(random_number)

    return result, expression
