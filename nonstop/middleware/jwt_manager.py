from jwt import encode, decode
from dotenv import dotenv_values

env = dotenv_values(".env")

def create_token(data: dict):
    token: str = encode(payload=data, key=env.get("SECRET_KEY"), algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    data: dict = decode(token, key=env.get("SECRET_KEY"), algorithms=["HS256"])
    return data