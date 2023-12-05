from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class UserModel(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    user = Column(String(50), unique=True)
    password = Column(String(500))