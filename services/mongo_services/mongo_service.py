from .mongo_query import MongoCommonds

class MongoService:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(MongoService, cls).__new__(cls)
        return cls.__instance

    def mongoCommondsInit(self, client, db):
        self.command = MongoCommonds(client, db)


mongoService = MongoService()
