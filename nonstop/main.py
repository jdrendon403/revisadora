from typing import Any, Coroutine, Optional
from fastapi import FastAPI, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from routes.status import status
from routes.users import users

from middleware.error_handler import ErrorHandler

from config.database import engine, Base
from config.db import inital_user
from models.user import UserModel

# from mangum import Mangum

app = FastAPI()
# handler = Mangum(app)

app.title = "NonStop Coms Interface"
app.version = "1.0"

app.add_middleware(ErrorHandler)
Base.metadata.create_all(bind=engine)

inital_user()

app.include_router(status)
app.include_router(users)

