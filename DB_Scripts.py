import sqlite3 as sql


def add_info(calc, res):
    try:
        sqlite_connection = sql.connect('CalculatorDB.db')
        execution = 'INSERT INTO History (Calculation, Result) VALUES (?, ?)'
        cursor = sqlite_connection.cursor()
        cursor.execute(execution, (calc, res))
        sqlite_connection.commit()
        cursor.close()
    except sql.Error as error:
        print('Fail to connect to sqlite', error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print('Connection to sqlite closed')


def load_info():
    try:
        sqlite_connection = sql.connect('CalculatorDB.db')
        execution = 'SELECT * FROM History'
        cursor = sqlite_connection.cursor()
        cursor.execute(execution)
        rows = cursor.fetchall()
        sqlite_connection.commit()
        cursor.close()
        return rows
    except sql.Error as error:
        print('Fail to connect to sqlite', error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            print('Connection to sqlite closed')
