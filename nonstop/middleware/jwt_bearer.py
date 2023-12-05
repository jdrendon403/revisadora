from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer
from config.database import Session
from middleware.jwt_manager import validate_token
from models.user import UserModel
from utilites.user_m import UserM

users = UserM()

class JWTBearer(HTTPBearer):
    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if not users.check_user(data['user']):
            if not Session().query(UserModel).filter(UserModel.user == data['user']).first():
                raise HTTPException(status_code=403, detail="Invalid credentials")
            else:
                users.add_user(data['user'])
            Session().close()
