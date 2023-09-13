import sqlite3 as sql
import logging


def add_info(calc, res):
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')
    try:
        sqlite_connection = sql.connect('CalculatorDB.db')
        logging.info('Connection to sqlite opened')
        execution = 'INSERT INTO History (Calculation, Result) VALUES (?, ?)'
        cursor = sqlite_connection.cursor()
        cursor.execute(execution, (calc, res))
        sqlite_connection.commit()
        cursor.close()
    except sql.Error as error:
        logging.error('Fail to connect to sqlite', error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            logging.info('Connection to sqlite closed')


def load_info():
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')
    try:
        sqlite_connection = sql.connect('CalculatorDB.db')
        logging.info('Connection to sqlite opened')
        execution = 'SELECT * FROM History'
        cursor = sqlite_connection.cursor()
        cursor.execute(execution)
        rows = cursor.fetchall()
        sqlite_connection.commit()
        cursor.close()
        return rows
    except sql.Error as error:
        logging.error('Fail to connect to sqlite', error)
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            logging.info('Connection to sqlite closed')
