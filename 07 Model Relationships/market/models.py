from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    id = Column(Integer(), primary_key=True)
    username = Column(String(length=30), nullable=False, unique=True)
    email_address = Column(String(length=50), nullable=False, unique=True)
    password_hash = Column(String(length=60), nullable=False)
    budget = Column(Integer(), nullable=False, default=1000)
    items = relationship('Item', backref='owned_user', lazy=True)



class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer(), primary_key=True)
    name = Column(String(length=30), nullable=False, unique=True)
    price = Column(Integer(), nullable=False)
    barcode = Column(String(length=12), nullable=False, unique=True)
    description = Column(String(length=1024), nullable=False, unique=True)
    owner = Column(Integer(), ForeignKey('user.id'))

    def __repr__(self):
        return f'Item {self.name}'




