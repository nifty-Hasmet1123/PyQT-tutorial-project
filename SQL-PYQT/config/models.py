from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

# from config.db import engine

# create your models here
Base = declarative_base()

class ExpenseModel(Base):
    __tablename__ = "expenses"

    id = Column(Integer(), primary_key=True, autoincrement=True)
    date = Column(DateTime(), default=datetime.now)
    category = Column(String(255))
    amount = Column(Float())
    description = Column(String(255))

    def __init__(self, category, amount, description, **kwargs):
        super().__init__(**kwargs)
        self.category = category
        self.amount = amount
        self.description = description


# add the table to dadtabase
# Base.metadata.create_all(engine)