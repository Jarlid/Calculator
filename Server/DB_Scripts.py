import sqlite3 as sql
import logging
from datetime import datetime


def add_info(calc, res):
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')
    try:
        sqlite_connection = sql.connect('Calculator_DB.db', )
        logging.info('Connection to sqlite opened' + datetime.now().strftime(' %H:%M:%S'))
        execution = 'INSERT INTO History (Calculation, Result) VALUES (?, ?)'
        cursor = sqlite_connection.cursor()
        cursor.execute(execution, (calc, res))
        sqlite_connection.commit()
        cursor.close()
    except sql.Error as error:
        logging.error('Fail to connect to sqlite' + error.sqlite_errorname + datetime.now().strftime(' %H:%M:%S'))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            logging.info('Connection to sqlite closed' + datetime.now().strftime(' %H:%M:%S'))


def load_info():
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')
    try:
        sqlite_connection = sql.connect('Calculator_DB.db')
        logging.info('Connection to sqlite opened' + datetime.now().strftime(' %H:%M:%S'))
        execution = 'SELECT * FROM History'
        cursor = sqlite_connection.cursor()
        cursor.execute(execution)
        rows = cursor.fetchall()
        sqlite_connection.commit()
        cursor.close()
        return rows
    except sql.Error as error:
        logging.error('Fail to connect to sqlite' + error.sqlite_errorname + datetime.now().strftime(' %H:%M:%S'))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            logging.info('Connection to sqlite closed' + datetime.now().strftime(' %H:%M:%S'))
