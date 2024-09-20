import string
import random

LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
SYMBOLS = string.punctuation
NUMBERS = string.digits

ALL_CHARS = LOWERCASE + UPPERCASE + SYMBOLS + NUMBERS


def password_generator():

    length = int(input('How long do you want your password to be? : ').strip())

    # some sites require everything in your password.
    number = random.choice(NUMBERS)
    upper = random.choice(UPPERCASE)
    lower = random.choice(LOWERCASE)
    symbol = random.choice(SYMBOLS)

    combination = [number + upper + lower + symbol]

    if length <= 0:
        print('Please enter a number bigger than zero.')
        raise ValueError

    elif length < 4:
        chars = random.choices(ALL_CHARS, k=length)

        return ''.join(chars)

    else:
        chars = random.choices(ALL_CHARS, k=length-4)

        return ''.join(combination + chars)


def main():

    try:
        print(password_generator())

    except ValueError:
        print('please enter a valid number.')
        main()


main()
