import random

random_number = random.randint(0, 50)
guess_count = 3
guess_was_right = False

print(f'Random number is {random_number}')

def validate_guess(value: int, guess: int):
    if value == guess:
        print(f'Your guess {guess} is right!')
        return True
    elif value < guess:
        print(f'Your guess {guess} is too high')
        return False
    elif value > guess:
        print(f'Your guess {guess} is too low')
        return False


print('\nTry to guess my number (between 0 and 50).')

while guess_count > 0:

    print(f'\nYou have {guess_count} guesses.')

    try:
        guess = int(input('\nWhat''s your guess? '))
        result = validate_guess(random_number, guess)
        if result:
            guess_was_right = True
            break
        else:
            guess_count -= 1
    except:
        print('\nYour input was invalid')
        guess_count -= 1

if guess_was_right == False: 
    print('\n You didn''t guess correctly! Please play again!')