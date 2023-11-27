import sqlite3
from prettytable import from_db_cursor
from datetime import datetime



def make_database():
    with sqlite3.connect('table.db') as squliteconnction:
        cursor = squliteconnction.cursor()

        cursor.execute('''CREATE TABLE IF NOT EXISTS NOTE 
                        (id INTEGER PRIMARY KEY AUTOINCREMENT
                        ,note text
                    ,date text
                       ,time text)''')


def insert(note):

    date = datetime.now().strftime("%Y-%m-%d")
    time = datetime.now().strftime("%H:%M")
    insert_query = "INSERT INTO NOTE (note,date,time) VALUES (?,?,?)"
    values = (note, date, time)

    with sqlite3.connect('table.db') as squliteconnction:
        cursor = squliteconnction.cursor()
        cursor.execute(insert_query, values)


def show():
    with sqlite3.connect('table.db') as squliteconnction:
        cursor = squliteconnction.cursor()
        cursor.execute('SELECT * FROM NOTE')
        table = from_db_cursor(cursor)

    print(table)


def show_by_id(id):

    with sqlite3.connect('table.db') as squliteconnction:
        cursor = squliteconnction.cursor()
        query = 'SELECT * FROM NOTE WHERE id = ?'
        cursor.execute(query, id)
        table = from_db_cursor(cursor)
    print(table)


def search_by_note(word):
    with sqlite3.connect('table.db') as squliteconnction:
        cursor = squliteconnction.cursor()
        query = 'SELECT * FROM NOTE WHERE note like ? '
        cursor.execute(query, word)
        table = from_db_cursor(cursor)
    print(table)


def delete(id):

    alert = input('are you sure? this action can not be undone.(y/n)')
    if alert.lower() == 'y':
        with sqlite3.connect('table.db') as squliteconnction:
            cursor = squliteconnction.cursor()
            query = 'DELETE FROM NOTE where id = ?'
            cursor.execute(query, id)
            print('done')
    elif alert.lower() == 'n':
        print('operation cancled')

    else:
        print('please enter y or n')


def search_by_date(date):
    try:
        with sqlite3.connect('table.db') as squliteconnction:
            cursor = squliteconnction.cursor()
            query = 'SELECT * FROM note WHERE date = ? '
            cursor.execute(query, date)
            table = from_db_cursor(cursor)
        print(table)
    except sqlite3.ProgrammingError:
        print('Please enter a valid date. YYYY-MM-DD')
