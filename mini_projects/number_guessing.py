import random
import time

number = random.randint(1, 100)

while True:
    try:
        user_number = int(input('Enter a numbeer between 1 and 100: '))

        if user_number > 100 or user_number < 1:
            print('Invalid number. try again.')

        elif user_number > number:
            print('Too high!')

        elif user_number < number:
            print('Too low!')

        elif user_number == number:
            print('Correct!!')
            time.sleep(3)
            break

    except ValueError as e:
        print('Please enter a number.')
