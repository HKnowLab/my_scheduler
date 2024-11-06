###############################################################
# ※ JsonManager Class
#    - type(db, cfg)별로 json파일을 읽어서 전달
###############################################################

class JsonManager():
    def __init__(self, type, filename):
        self.__filename = filename
        self.__type = type
        self.__read()

    def get_read(self):
        if self.__type == "db":
            #TODO : 파싱
            self.__databaseInfo = None
            return self.__databaseInfo
        elif self.__type == "cfg":
            #TODO : 파싱
            self.__jobInfo = None
            return self.__jobInfo
        