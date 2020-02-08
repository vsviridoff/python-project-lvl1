from random import randint

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_gcd(first_number, second_number):
    min_number = min(first_number, second_number)
    max_number = max(first_number, second_number)

    devisor = 1
    while devisor <= min_number:
        if min_number % devisor == 0 and max_number % devisor == 0:
            correct_answer = str(devisor)
        devisor += 1
    return correct_answer


def logic_game():
    number_one = randint(1, 100)
    number_two = randint(1, 100)

    result = get_gcd(number_one, number_two)
    expression = "{} {}".format(number_one, number_two)

    return result, expression
