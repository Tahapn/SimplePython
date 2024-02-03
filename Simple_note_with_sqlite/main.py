from SQL import make_database, insert, search_by_note, show_by_id, delete, show, search_by_date
import sqlite3
import os.path as path
import time


#create DB for the first time or incase it's deleted
if not path.exists('table.db'):
    make_database()


def function_choice():

    operation = input(
        'What do you want to do? <show><insert><sbi(search by id)> <sbn(search by note)> <delete> sbd<search by date>  <exit> \n: ').strip()

    # I used the match case instead of a long if , elif statement

    match operation.lower() :
        case 'insert':
            user_note = str(input('Please insert your note:'))
            insert(user_note)
            print('Done\n')

            function_choice()
        
        case 'show':
            show()
            function_choice()

        # | is for running the same code with two different inputs
        case 'serach by id' | 'sbi':
            user_id = input('please enter id of the note:')
            try:
                show_by_id(user_id)

            except sqlite3.ProgrammingError:
                print('please enter a valid number')

            
            function_choice()

        case 'serach by note' | 'sbn':
            user_input = input(
                'enter the word that you think is in the note you want to find.\n:')
            
            #fixed is for handeling a error .

            fixed = ('%' + user_input + '%',)

            search_by_note(fixed)
            function_choice()

        
        case 'search by date' | 'sbd':
            user_input = input(
                'enter notes inserted in desired date.YYYY-MM-DD\n:')
            fixed = (user_input,)
            search_by_date(fixed)
            function_choice()
        
        case 'delete':
            try:
                delete(input('enter the id of the row that you want to delete.'))
                function_choice()
            except sqlite3.ProgrammingError:
                print('please enter a valid number')
                function_choice()

        case 'exit' : 
            print('Bye')
            time.sleep(3)

        case _ :
            print('invalid input. please enter one of these words : (show,insert,sbi,sbn,delete)')
            function_choice()

function_choice()

