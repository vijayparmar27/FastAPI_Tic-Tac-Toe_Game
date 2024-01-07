import uvicorn
from connection.mongodb import mongoConnection 
from connection.socket import socket_io_app

mongoConnection.connect()

app = socket_io_app.app

if __name__ == "__main__":

    print("server ::")
    # uvicorn.run("main:app",port=3000)
    # uvicorn.run("main:app",port=3000,reload=True)
    uvicorn.run("connection.socket:app",port=3000,reload=True)
    # uvicorn.run(app,port=3000,reload=True)
    # uvicorn.run(app,port=3000)