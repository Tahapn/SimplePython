from random import randint
from time import sleep
from os import system
from rich.console import Console


def main():

    console = Console()

    number = randint(1_000_000,9_999_999)
    console.print(f'The number is [bold green] {number:,d} [/bold green]')

    n = 5
    while n != -1:
        console.print(f' clear screen in [bold red] {n} [/bold red] seconds' , end='\r')
        n-=1
        sleep(0.9)

    system('cls')

    while True:
        try:
            user_input = int(input('What was the number? : '))
            break
        except ValueError:
            console.print('[bold red] Please enter a valid number [/bold red]')

    if user_input == number :
        console.print('[bold green] YES YOU WIN [/bold green]')
    else :
        console.print('[bold red] NO YOU LOSE [/bold red]')

    console.print(f'The number was [bold blue] {number:,d} [/bold blue] ')

    replay()


def replay():
    user = input('Do you want to play again? ')

    if user.lower() == 'y':
        main()
    elif user.lower() == 'n':
        print('Okay goodbye')

    else : 
        print('please enter either Y or N. ')
        replay()
    
main()