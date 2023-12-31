from pymongo import MongoClient
from services.mongo_services.mongo_service import mongoService

class MongoConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MongoConnection, cls).__new__(cls)
        return cls.__instance

    def connect(self):
        self.__client = MongoClient("mongodb://localhost:27017/")
        self.__db = self.__client["fastAPI_Tic-Tac-Tie"]
        # self.__db = self.__client["allData"].users.insert_one()
        mongoService.mongoCommondsInit(self.__client,self.__db)  


mongoConnection = MongoConnection()