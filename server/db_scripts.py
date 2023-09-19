import sqlite3 as sql
from datetime import datetime
import logging
from db_config import DB_NAME, TABLE_NAME, LOG_FILE_NAME, BASIC_LEVEL_OF_LOGGING, ERROR_MESSAGE, \
    CONNECTION_TO_SQLITE_CLOSED, CONNECTION_TO_SQLITE_OPENED, TABLE_SQLITE_CREATED, SUCC_SELECT, SUCC_INSERT


class DBException(Exception):
    """Throwing errors with db outside"""
    pass


def add_info(calc, res):
    logging.basicConfig(level=BASIC_LEVEL_OF_LOGGING, filename=LOG_FILE_NAME, filemode='a')
    sqlite_connection = None
    try:
        sqlite_connection = sql.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        logging.info(CONNECTION_TO_SQLITE_OPENED.format(time=datetime.utcnow().strftime('%H:%M:%S')))
        query = f''' INSERT INTO {TABLE_NAME}(Calculation, Result) VALUES (?, ?) '''
        cursor.execute(query, (calc, res))
        sqlite_connection.commit()
        logging.info(SUCC_INSERT.format(time=datetime.utcnow().strftime('%H:%M:%S')))
        cursor.close()
    except sql.Error as error:
        logging.error(ERROR_MESSAGE.format(time=datetime.utcnow().strftime('%H:%M:%S')) + repr(error))
        if sqlite_connection:
            sqlite_connection.close()
            logging.info(CONNECTION_TO_SQLITE_CLOSED.format(time=datetime.utcnow().strftime('%H:%M:%S')))
        raise DBException("Can't insert into the db, " + repr(error))
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            logging.info(CONNECTION_TO_SQLITE_CLOSED.format(time=datetime.utcnow().strftime('%H:%M:%S')))


def load_info() -> str:
    """Return a string in format [Calculation]$[Result]$[Calculation]$[Result]..."""
    logging.basicConfig(level=BASIC_LEVEL_OF_LOGGING, filename=LOG_FILE_NAME, filemode='a')
    sqlite_connection = None
    try:
        sqlite_connection = sql.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        logging.info(CONNECTION_TO_SQLITE_OPENED.format(time=datetime.utcnow().strftime('%H:%M:%S')))
        query = f''' SELECT * FROM {TABLE_NAME} '''
        cursor.execute(query)
        rows = cursor.fetchall()
        sqlite_connection.commit()
        logging.info(SUCC_SELECT.format(time=datetime.utcnow().strftime('%H:%M:%S')))
        cursor.close()
        rows = '$'.join(map(lambda x: x[1] + '$' + x[2], rows))
        return rows
    except sql.Error as error:
        logging.error(ERROR_MESSAGE.format(time=datetime.utcnow().strftime('%H:%M:%S')) + repr(error))
        if sqlite_connection:
            sqlite_connection.close()
            logging.info(CONNECTION_TO_SQLITE_CLOSED.format(time=datetime.utcnow().strftime('%H:%M:%S')))
        raise DBException("Can't load from the db, " + repr(error))
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            logging.info(CONNECTION_TO_SQLITE_CLOSED.format(time=datetime.utcnow().strftime('%H:%M:%S')))


def create_db():
    logging.basicConfig(level=BASIC_LEVEL_OF_LOGGING, filename=LOG_FILE_NAME, filemode='a')
    sqlite_connection = None
    try:
        sqlite_connection = sql.connect(DB_NAME)
        sqlite_create_table_query = f''' CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                                        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL DEFAULT 1 UNIQUE,
                                        Calculation TEXT NOT NULL,
                                        Result TEXT NOT NULL
                                        ); '''
        cursor = sqlite_connection.cursor()
        logging.info(CONNECTION_TO_SQLITE_OPENED.format(time=datetime.utcnow().strftime('%H:%M:%S')))
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        logging.info(TABLE_SQLITE_CREATED.format(time=datetime.utcnow().strftime('%H:%M:%S')))

    except sql.Error as error:
        logging.error(ERROR_MESSAGE.format(time=datetime.utcnow().strftime('%H:%M:%S')) + repr(error))
        if sqlite_connection:
            sqlite_connection.close()
            logging.info(CONNECTION_TO_SQLITE_CLOSED.format(time=datetime.utcnow().strftime('%H:%M:%S')))
        raise DBException("Can't create a db, " + repr(error))
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            logging.info(CONNECTION_TO_SQLITE_CLOSED.format(time=datetime.utcnow().strftime('%H:%M:%S')))
