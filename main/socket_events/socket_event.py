import json

async def event_send(socketId, data):
    from connection.socket import socket_io_app
    sio = socket_io_app.sio
    print("------- event_send :: socketId ::",socketId)
    # data = vars(data) # if data is SimpleNamespace
    # data = {"name" : "dev"}
    await sio.emit(event=data["en"], data=json.dumps(data), room=socketId)

async def addInRoom(socketId,room):
    from connection.socket import socket_io_app
    sio = socket_io_app.sio
    await sio.enter_room(sid=socketId,room=room)

# async def removeFromRoom(socketId,room):
#     sio = socket_io_app.sio
#     await sio.leave_room(sid=socketId,room=room)
#     return ""
