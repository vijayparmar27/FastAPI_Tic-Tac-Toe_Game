from pymongo import MongoClient


class MongoConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MongoConnection, cls).__new__(cls)
        return cls.__instance

    def connect(self):
        self.__client = MongoClient("mongodb://localhost:27017/")
        self.__db = self.__client["allData"]

    @property
    def client(self):
        return self.__client    
    
    @property
    def db(self):
        return self.__db    


mongoConnection = MongoConnection()