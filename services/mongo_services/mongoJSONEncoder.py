import json
from bson import ObjectId

class CustomMongoJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, ObjectId):
            return str(obj)
        return super().default(obj)

    @classmethod
    def mongoDataStringify(cls, data):
        info = json.loads(json.dumps(data, cls=cls))
        return info