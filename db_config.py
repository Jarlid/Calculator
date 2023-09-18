from datetime import datetime
import logging

DB_NAME = 'Calculator_db.db'
TABLE_NAME = 'History'
LOG_FILE_NAME = 'py_log.log'
BASIC_LEVEL_OF_LOGGING = logging.INFO
ERROR_MESSAGE = f'''{datetime.utcnow().strftime('%H:%M:%S')}: Fail to operate with sqlite, '''
CONNECTION_TO_SQLITE_OPENED = f'''{datetime.utcnow().strftime('%H:%M:%S')}: Connection to sqlite opened'''
CONNECTION_TO_SQLITE_CLOSED = f'''{datetime.utcnow().strftime('%H:%M:%S')}: Connection to sqlite closed'''
TABLE_SQLITE_CREATED = f'''{datetime.utcnow().strftime('%H:%M:%S')}: Table sqlite exist'''
SUCC_INSERT = f'''{datetime.utcnow().strftime('%H:%M:%S')}: Recordings successfully inserted into a table History'''
SUCC_SELECT = f'''{datetime.utcnow().strftime('%H:%M:%S')}: Recordings successfully selected from a table History'''