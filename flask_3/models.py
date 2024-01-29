from main import db
from sqlalchemy import String, Column, Integer


class User(db.Model):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(16))
    last_name = Column(String(16))
    email = Column(String(64))
    hash_pswd = Column(String())

    def __repr__(self):
        return f'User({self.__dict__})'
