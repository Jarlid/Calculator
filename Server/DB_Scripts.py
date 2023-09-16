import sqlite3 as sql
import logging
from datetime import datetime


def add_info(calc, res):
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')
    try:
        sqlite_connection = sql.connect('Calculator_DB.db', )
        cursor = sqlite_connection.cursor()
        logging.info('Connection to sqlite opened' + datetime.utcnow().strftime(' %H:%M:%S'))
        execution = 'INSERT INTO History (Calculation, Result) VALUES (?, ?)'
        cursor.execute(execution, (calc, res))
        sqlite_connection.commit()
        logging.info(
            'Recording successfully inserted into a table History' + datetime.utcnow().strftime(' %H:%M:%S'))
        cursor.close()
    except sql.Error as error:
        logging.error('Fail to connect to sqlite' + error.sqlite_errorname + datetime.utcnow().strftime(' %H:%M:%S'))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            logging.info('Connection to sqlite closed' + datetime.utcnow().strftime(' %H:%M:%S'))


def load_info():
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')
    try:
        sqlite_connection = sql.connect('Calculator_DB.db')
        cursor = sqlite_connection.cursor()
        logging.info('Connection to sqlite opened' + datetime.utcnow().strftime(' %H:%M:%S'))
        execution = 'SELECT * FROM History'
        cursor.execute(execution)
        rows = cursor.fetchall()
        sqlite_connection.commit()
        logging.info(
            'Recordings successfully selected from a table History' + datetime.utcnow().strftime(' %H:%M:%S'))
        cursor.close()
        rows = '#'.join(map(lambda x: x[1] + '#' + x[2], rows))
        return rows
    except sql.Error as error:
        logging.error('Fail to connect to sqlite' + error.sqlite_errorname + datetime.utcnow().strftime(' %H:%M:%S'))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            logging.info('Connection to sqlite closed' + datetime.utcnow().strftime(' %H:%M:%S'))


def create_DB():
    logging.basicConfig(level=logging.INFO, filename='py_log.log', filemode='w')
    try:
        sqlite_connection = sql.connect('Calculator_DB.db')
        sqlite_create_table_query = '''CREATE TABLE History (
                                        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL DEFAULT 1 UNIQUE,
                                        Calculation TEXT NOT NULL,
                                        Result TEXT NOT NULL
                                        );'''
        cursor = sqlite_connection.cursor()
        logging.info('Connection to sqlite opened' + datetime.utcnow().strftime(' %H:%M:%S'))
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        logging.info('Table sqlite created' + datetime.utcnow().strftime(' %H:%M:%S'))

    except sql.Error as error:
        logging.error('Fail to connect to sqlite' + error.sqlite_errorname + datetime.utcnow().strftime(' %H:%M:%S'))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            logging.info('Connection to sqlite closed' + datetime.utcnow().strftime(' %H:%M:%S'))
