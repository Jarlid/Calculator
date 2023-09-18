import sqlite3 as sql
from db_config import *


def add_info(calc, res):
    logging.basicConfig(level=BASIC_LEVEL_OF_LOGGING, filename=LOG_FILE_NAME, filemode='w')
    try:
        sqlite_connection = sql.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        logging.info(CONNECTION_TO_SQLITE_OPENED)
        execution = f''' INSERT INTO {TABLE_NAME}(Calculation, Result) VALUES (?, ?) '''
        cursor.execute(execution, (calc, res))
        sqlite_connection.commit()
        logging.info(SUCC_INSERT)
        cursor.close()
    except sql.Error as error:
        logging.error(ERROR_MESSAGE + repr(error))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            logging.info(CONNECTION_TO_SQLITE_CLOSED)


def load_info() -> str:
    """Return a string in format [Calculation]$[Result]$[Calculation]$[Result]..."""
    logging.basicConfig(level=BASIC_LEVEL_OF_LOGGING, filename=LOG_FILE_NAME, filemode='w')
    try:
        sqlite_connection = sql.connect(DB_NAME)
        cursor = sqlite_connection.cursor()
        logging.info(CONNECTION_TO_SQLITE_OPENED)
        execution = f''' SELECT * FROM {TABLE_NAME} '''
        cursor.execute(execution)
        rows = cursor.fetchall()
        sqlite_connection.commit()
        logging.info(SUCC_SELECT)
        cursor.close()
        rows = '$'.join(map(lambda x: x[1] + '$' + x[2], rows))
        return rows
    except sql.Error as error:
        logging.error(ERROR_MESSAGE + repr(error))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            logging.info(CONNECTION_TO_SQLITE_CLOSED)


def create_db():
    logging.basicConfig(level=BASIC_LEVEL_OF_LOGGING, filename=LOG_FILE_NAME, filemode='w')
    try:
        sqlite_connection = sql.connect(DB_NAME)
        sqlite_create_table_query = f''' CREATE TABLE IF NOT EXISTS {TABLE_NAME} (
                                        Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL DEFAULT 1 UNIQUE,
                                        Calculation TEXT NOT NULL,
                                        Result TEXT NOT NULL
                                        ); '''
        cursor = sqlite_connection.cursor()
        logging.info(CONNECTION_TO_SQLITE_OPENED)
        cursor.execute(sqlite_create_table_query)
        sqlite_connection.commit()
        logging.info(TABLE_SQLITE_CREATED)

    except sql.Error as error:
        logging.error(ERROR_MESSAGE + repr(error))
    finally:
        if (sqlite_connection):
            sqlite_connection.close()
            logging.info(CONNECTION_TO_SQLITE_CLOSED)



