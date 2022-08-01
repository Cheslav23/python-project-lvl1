import prompt


def welcome_user(who):
    who = prompt.string('May I have your name? ')
    print(f'Hello, {who}!')
