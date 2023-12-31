from .mongoJSONEncoder import CustomMongoJSONEncoder


class MongoCommonds:
    def __init__(self, client, db) -> None:
        self.client = client
        self.db = db
        self.json = CustomMongoJSONEncoder().mongoDataStringify

    async def find(self, collectionName, query={}):
        collection = self.db[collectionName]
        data = self.json(list(collection.find(query)))
        return None if len(data) == 0 else data

    async def findOne(self, collectionName, query):
        collection = self.db[collectionName]
        data = collection.find_one(query)
        return None if data is None else self.json(dict(data))
    
    async def insertOne(self, collectionName, details):
        collection = self.db[collectionName]
        data = collection.insert_one(details)
        return data.inserted_id if data else None
