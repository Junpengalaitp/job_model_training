import logging

import mysql.connector
from mysql.connector import errorcode
from mysql.connector import pooling

from logger.logger import setup_logging
from config import read_config

setup_logging()
logger = logging.getLogger("dbLogger")


class MysqlManager:
    DB_NAME = read_config.get_config('mysql', 'dbname')
    SERVER_IP = read_config.get_config('mysql', 'ip')
    PORT = read_config.get_config('mysql', 'port')

    def __init__(self, max_num_thread):
        username = read_config.get_config('mysql', 'user')
        password = read_config.get_config('mysql', 'password')
        try:
            cnx = mysql.connector.connect(host=self.SERVER_IP, port=self.PORT, user=username, password=password)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                logger.error("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                logger.error("Database does not exist")
            else:
                logger.error('Create Error ' + err.msg)
            exit(1)

        cursor = cnx.cursor()

        try:
            cnx.database = self.DB_NAME
        except mysql.connector.Error as err:
            logger.error(err)
            exit(1)
        finally:
            cursor.close()
            cnx.close()

        dbconfig = {
            "database": self.DB_NAME,
            "user": username,
            "host": self.SERVER_IP,
            "password": password,
            "port": self.PORT
        }
        self.cnxpool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool", pool_size=max_num_thread,
                                                                   **dbconfig)

    def insert(self, query):
        try:
            con = self.cnxpool.get_connection()
            cursor = con.cursor()
            cursor.execute(query)
            con.commit()
            logging.info(f'insert successful, query: {query}')
        except mysql.connector.Error as err:
            con.rollback()
            logging.error(f'insert error: {err.msg}, query: {query}')
            return
        finally:
            cursor.close()
            con.close()
