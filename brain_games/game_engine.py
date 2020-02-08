import brain_games.cli
import prompt
ROUNDS = 3


def start_game(name_game):
    greeting = 'Welcome to the Brain games!'
    print(greeting)
    print(name_game.DESCRIPTION)
    name = brain_games.cli.welcome_user()

    counter = 1
    while counter <= ROUNDS:
        result, expression = name_game.logic_game()
        question = 'Question: ' + expression

        print(question)
        response = prompt.string('Your answer: ')

        if response == result:
            if counter == ROUNDS:
                print('Correct!')
                print("Congratulations, {}!".format(name))
                break
            else:
                print('Correct!')
                counter += 1

        else:
            error_output = "'{}' is wrong answer ;(. ".format(response)
            correct_output = "Correct answer was '{}'.".format(result)
            print(error_output + correct_output)
            print("Let's try again, {}!".format(name))
            break
