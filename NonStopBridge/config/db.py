from config.database import Session
from models.status import StatusModel
from dotenv import dotenv_values


env = dotenv_values(".env")

def inital_data():
    db = Session()
    if not db.query(StatusModel).filter(StatusModel.id == 1).first():
        new_status = StatusModel(
            id=1,
            peso=0.0,
            metros=0.0,
            rendimiento=0.0,
        )
        db.add(new_status)
        db.commit()
    db.close()

def update_data(id_u, peso_u, metros_u, rendimiento_u):
    db = Session()
    db.query(StatusModel).filter(StatusModel.id == id_u).update({
        "peso": peso_u,
        "metros": metros_u,
        "rendimiento": rendimiento_u
    })
    db.commit()
    db.close()
