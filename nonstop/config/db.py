from fastapi import Depends
from config.database import Session
from typing import Annotated
from models.user import UserModel
from passlib.context import CryptContext
from dotenv import dotenv_values


env = dotenv_values(".env")

def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

def inital_user():
    db = Session()
    if not db.query(UserModel).filter(UserModel.user == "admin").first():
        bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        new_user = UserModel(
            user="admin",
            password=bcrypt_context.hash(env.get("INI_PASSWORD")),
        )
        db.add(new_user)
        db.commit()
    db.close()