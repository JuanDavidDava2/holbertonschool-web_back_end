#!/usr/bin/env python3
"""0x05. Personal data"""

import re
from typing import List
import logging
import mysql.connector
from os import getenv

PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """Regex-ing"""
    for item in fields:
        message = re.sub(fr'{item}=.+?{separator}',
                         f'{item}={redaction}{separator}', message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Implement the format method to filter values in incoming log
        records using filter_datum.
        Values for fields in fields should be filtered
        """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def get_logger() -> logging.Logger:
    """Create logger
        returns a logging.Logger object
    """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Connect to secure database
        returns a connector to the database
    """
    db = mysql.connector.connection.MySQLConnection(
            user=getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
            password=getenv('PERSONAL_DATA_DB_PASSWORD', ''),
            host=getenv('PERSONAL_DATA_DB_HOST', 'localhost'),
            database=getenv('PERSONAL_DATA_DB_NAME'))

    return db


def main():
    """Read and filter data
    Implement a main function that takes no arguments and returns nothing.
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")

    result = cursor.fetchall()
    for data in result:
        message = f"name={data[0]}; " + \
                  f"email={data[1]}; " + \
                  f"phone={data[2]}; " + \
                  f"ssn={data[3]}; " + \
                  f"password={data[4]}; " + \
                  f"ip={data[5]}; " + \
                  f"last_login={data[6]}; " + \
                  f"user_agent={data[7]};"
        print(message)
        log_record = logging.LogRecord("my_logger", logging.INFO,
                                       None, None, message, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        formatter.format(log_record)
    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
