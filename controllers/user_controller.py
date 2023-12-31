from models.user_model import SignupRequest, LoginRequest
from services.mongo_services.mongo_service import mongoService
from services.mongo_services.mongoJSONEncoder import CustomMongoJSONEncoder
from fastapi import status
from fastapi.responses import JSONResponse
from utils.hash import Hash
from utils.token import Token


async def signupController(request: SignupRequest):

    if not request.userName or not request.lastName or not request.userName or not request.phoneNo or not request.password or not request.confPassword:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
            "status": False,
            "message": "fill all fields !",
            "statusCode": status.HTTP_400_BAD_REQUEST,
            "data": None
        })

    if request.password != request.confPassword:
        return JSONResponse(status_code=status.HTTP_226_IM_USED, content={
            "status": False,
            "message": "Comfirm Password Not Same !",
            "statusCode": status.HTTP_406_NOT_ACCEPTABLE,
            "data": None
        })

    query = {
        "$or": [
            {"userName": request.userName},
            {"phoneNo": request.phoneNo},
        ]
    }

    data = await mongoService.command.findOne("users", query)

    if (data):
        return JSONResponse(status_code=status.HTTP_226_IM_USED, content={
            "status": False,
            "message": "Account aleady exsist !",
            "statusCode": status.HTTP_226_IM_USED,
            "data": None
        })
    hashed_password = Hash.get_hash(request.password)
    print("--------  Hash.get_hash(request.password) :: ", hashed_password)

    insert_data = {
        "firstName": request.firstName,
        "lastName": request.lastName,
        "userName": request.userName,
        "phoneNo": request.phoneNo,
        "password": Hash.get_hash(request.password),
    }

    res_data = await mongoService.command.insertOne("users", insert_data)

    if (res_data):
        return JSONResponse(status_code=status.HTTP_201_CREATED, content={
            "status": True,
            "message": "Acoount has created !",
            "statusCode": status.HTTP_201_CREATED,
            "data": None
        })

    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
        "status": True,
        "message": "some issue from server side !",
        "statusCode": status.HTTP_400_BAD_REQUEST,
        "data": None
    })


async def loginController(request: LoginRequest):

    if not request.uniqueId or not request.password:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={
            "status": False,
            "message": "fill all fields !",
            "statusCode": status.HTTP_400_BAD_REQUEST,
            "data": None
        })

    query = {
        "$or": [
            {"userName": request.uniqueId},
            {"phoneNo": request.uniqueId},
        ]
    }

    data = await mongoService.command.findOne("users", query)
    is_valid_password = Hash.verify_hash(request.password, data["password"])

    if not is_valid_password:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content={
            "status": False,
            "message": "Invalid Password !",
            "statusCode": status.HTTP_401_UNAUTHORIZED,
            "data": None
        })

    print("--- data._id :: ", data["_id"])

    generat_token = Token.create_access_token({"id": data["_id"]})

    del data["password"]

    return JSONResponse(status_code=status.HTTP_200_OK, content={
        "status": True,
        "message": "Login Successfuly !",
        "statusCode": status.HTTP_200_OK,
        "data": {
            "accessToken": generat_token,
            "userInfo":  data
        }
    })
