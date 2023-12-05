from fastapi import APIRouter, Body, status as httpstatus, Depends
from fastapi.responses import JSONResponse

from middleware.jwt_manager import create_token
from middleware.jwt_bearer import JWTBearer
from config.database import Session
from schemas.user import User
from services.user import UserService

from config.db import db_dependency, get_db


users = APIRouter()


@users.post("/login/",
           tags=["Auth"]
           )
def login(db: db_dependency, user: User = Body(...)):
    # db = Session()
    if not UserService(db).validate_user(user):
        return JSONResponse(content=False, status_code=httpstatus.HTTP_401_UNAUTHORIZED)
    token = {"token": create_token(user.model_dump())}
    return JSONResponse(content=token, status_code=httpstatus.HTTP_201_CREATED)

@users.post("/create_user/",
            tags=["Auth"],
            dependencies=[Depends(JWTBearer())]
            )
def create_user(db: db_dependency, user: User = Body(...)):
    # db = Session()
    UserService(db).create_user(user)
    return JSONResponse(content=user.model_dump(), status_code=httpstatus.HTTP_201_CREATED)
