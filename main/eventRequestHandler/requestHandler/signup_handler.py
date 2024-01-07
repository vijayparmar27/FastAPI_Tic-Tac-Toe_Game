from models.eventRequest_model import signupEventReq
from middlewares.auth import Token
from ...socket_events.socket_event import event_send
from ...formateResponce.common_popup import common_popup_formate
from constant.massages.index import MESSAGES
from services.mongo_services.mongo_service import mongoService
from bson import ObjectId


async def signupHandler(socketId, data: signupEventReq, io):
    # if data is SimpleNamespace
    print("----- signupHandler :: data :: ", vars(data))

    if hasattr(data, 'token'):  # for check dict has property or not
        userId = await Token.verify_token_for_event(data.token)
        print("------- signupHandler :: userId :: ", userId)
        if not userId:
            res = common_popup_formate("Invalid Token !", 1, [MESSAGES.POPUP.BUTTON_TEXT.EXIT], [
                                       MESSAGES.POPUP.BUTTON_COLOR.RED], [MESSAGES.POPUP.BUTTON_METHOD.EXIT])
            await event_send(socketId, res)
            return
    else:
        res = common_popup_formate("token unavailble !", 1, [MESSAGES.POPUP.BUTTON_TEXT.EXIT], [
                                   MESSAGES.POPUP.BUTTON_COLOR.RED], [MESSAGES.POPUP.BUTTON_METHOD.EXIT])
        await event_send(socketId, res)
        return

    userData = await mongoService.command.findOne(
        "users",
        {"_id": ObjectId(userId)}
    )

    print("---- userdata : ", userData)

    if userData :
        await io.save_session(socketId, {'username': data.name})
        pass
    else:
        res = common_popup_formate("user not found !", 1, [MESSAGES.POPUP.BUTTON_TEXT.EXIT], [
                                   MESSAGES.POPUP.BUTTON_COLOR.RED], [MESSAGES.POPUP.BUTTON_METHOD.EXIT])
        await event_send(socketId, res)
        return


    

    session = await io.get_session(socketId)
    print('message from ', session['username'])
    return "data...."
