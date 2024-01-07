from dotenv import load_dotenv
import os
import json
load_dotenv()

port_value = os.environ.get("PORT")


port_value = json.loads(json.dumps({
    "key" : "value"
}))