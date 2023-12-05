from schemas.user import User
from models.user import UserModel


from passlib.context import CryptContext

class UserService():

    def __init__(self, db) -> None:
        self.db = db

    def create_user(self, user: User):
        bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        new_user = UserModel(
            user=user.user,
            password=bcrypt_context.hash(user.password),
        )
        self.db.add(new_user)
        self.db.commit()
        return
    
    def validate_user(self, user: User):
        bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        dbuser = self.db.query(UserModel).filter(UserModel.user == user.user).first()
        if not dbuser:
            return False
        if not bcrypt_context.verify(user.password, dbuser.password):
            return False
        return True