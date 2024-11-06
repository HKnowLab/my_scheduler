import mysql.connector

from db import databaseInfo

class DatabaseManager():
    def __init__(self, databaseInfo:databaseInfo.DatabaseInfo):
        pass

    def connect(self):
        try:
            self.__conn = mysql.connector.connect(host="localhost",
                                                    user="KABANG",
                                                    password="KABANG",
                                                    database="KABANG")
        except Exception as e:
            # TODO : 예외처리
            pass

        finally:
            self.disconnect()

        
    def disconnect(self):
        if self.__conn is not None:
            self.__conn.close()

        if self.__cursor is not None:
            self.__cursor.close()

    def execute(self, sql):
        self.__cursor = self.__conn.cursor()
        self.__cursor.excute(sql)
        self.__conn.commit()