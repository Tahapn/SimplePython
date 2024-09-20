import random
import time


while True:
    user_inupt = input('Roll the dice?(y/n):').lower().strip()

    match user_inupt:
        case 'y':
            num_one = random.choice(range(1, 7))
            num_two = random.choice(range(1, 7))
            print(f'({num_one}, {num_two})')
        case 'n':
            print('Okay goodbye')
            time.sleep(3)
            break
        case _:
            print('Invalid input. Please enter y or n.')
