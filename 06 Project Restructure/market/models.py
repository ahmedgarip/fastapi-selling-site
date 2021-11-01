from sqlalchemy import Column, Integer, String, ForeignKey
from database import Base


class Item(Base):
    __tablename__ = 'items'

    id = Column(Integer(), primary_key=True)
    name = Column(String(length=30), nullable=False, unique=True)
    price = Column(Integer(), nullable=False)
    barcode = Column(String(length=12), nullable=False, unique=True)
    description = Column(String(length=1024), nullable=False, unique=True)

    def __repr__(self):
        return f'Item {self.name}'




