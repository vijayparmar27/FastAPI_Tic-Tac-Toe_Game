import uvicorn
from connection.server import app
from connection.mongodb import mongoConnection 

mongoConnection.connect()

if __name__ == "__main__":
    print("server ::")
    # uvicorn.run("main:app",port=3000)
    uvicorn.run("main:app",port=3000,reload=True)
    # uvicorn.run(app,port=3000)
