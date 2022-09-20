import random


def guess(x):
    random_number = random.randint(10, 30)

    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 10 and {x}: '))
        if guess < random_number:
            print('Sorry guess again your number is too low!')
        elif guess > random_number:
            print('Sorry try again your number is too high!')

    print(f'Congratulations you have guessed the number {random_number} right !!')


guess(30)
