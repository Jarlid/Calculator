import logging

DB_NAME = 'calculator_db.db'
TABLE_NAME = 'History'
LOG_FILE_NAME = 'py_log.log'
BASIC_LEVEL_OF_LOGGING = logging.INFO
ERROR_MESSAGE = '''{time}: Fail to operate with sqlite, '''
CONNECTION_TO_SQLITE_OPENED = '''{time}: Connection to sqlite opened'''
CONNECTION_TO_SQLITE_CLOSED = '''{time}: Connection to sqlite closed'''
TABLE_SQLITE_CREATED = '''{time}: Table sqlite exist'''
SUCC_INSERT = '''{time}: Recordings successfully inserted into a table History'''
SUCC_SELECT = '''{time}: Recordings successfully selected from a table History'''
