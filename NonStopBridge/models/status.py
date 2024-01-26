from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class StatusModel(Base):

    __tablename__ = "status"

    id = Column(Integer, primary_key=True)
    peso = Column(Float)
    metros = Column(Float)
    rendimiento = Column(Float)