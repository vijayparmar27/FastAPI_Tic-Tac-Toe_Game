from constant.index import CONSTANT
import json
from .requestHandler.signup_handler import signupHandler
from types import SimpleNamespace


async def requestHandler(event, sid, payload, io):
    payload = json.loads(payload) if type(payload) == str else payload

    if CONSTANT.EVENT.HEART_BEAT is not event:
        print("----- requestHandler :: EVENT :: ", event)
        print("----- requestHandler :: payload :: ", payload)

    data = SimpleNamespace(**payload["data"])
    print("----- requestHandler :: data :: ", data, type(data))

    match event:
        case CONSTANT.EVENT.HEART_BEAT:
            pass
        case CONSTANT.EVENT.SIGN_UP:
            return await signupHandler(sid, data, io)
        case CONSTANT.EVENT.LOBBY:
            pass
        case CONSTANT.EVENT.MATCH_MAKE:
            pass

        case _:
            print("default call :: requestHandler ::")
