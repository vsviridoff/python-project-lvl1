from random import randint

description = 'What number is missing in the progression?'


def logic_game():
    first_number = randint(1, 10)
    step = randint(1, 10)
    hidden_number = randint(0, 9)
    counter = 0
    progression = ''

    while counter <= 10:
        current_number = first_number + (counter * step)

        if counter == hidden_number:
            element = '.. '
            result = str(current_number)
        else:
            element = str(current_number) + " "

        progression += element
        counter += 1

    expression = '{}'.format(progression)

    return result, expression
