from random import randint

description = 'Find the greatest common divisor of given numbers.'


def logic_game():
    number_one = randint(1, 100)
    number_two = randint(1, 100)
    min_number = min(number_one, number_two)
    max_number = max(number_one, number_two)

    devisor = 1
    while devisor <= min_number:
        if min_number % devisor == 0 and max_number % devisor == 0:
            result = str(devisor)
        devisor += 1

    expression = "{} {}".format(number_one, number_two)
    question = 'Question: ' + expression

    return result, question
