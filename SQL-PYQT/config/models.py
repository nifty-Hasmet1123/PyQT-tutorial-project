from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship, validates
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

    # def __init__(self, category, amount, description, **kwargs):
    #     super().__init__(**kwargs)
    #     self.category = category
    #     self.amount = amount
    #     self.description = description

    @validates("category")
    def validate_category(self, key, value):
        # key is the column name
        # value is the data you are trying to put inside the column
        if not value:
            raise AssertionError("Category data should not be empty.")

        return value.strip()
    
    @validates("amount")
    def validate_amount(self, key, value):
        try:
            value = float(value)
            if not isinstance(value, (float, int)):
                raise AssertionError("Amount should be a number.")
            if value < 0:
                raise AssertionError("Amount should be an absolute number")
        except ValueError:
            raise AssertionError("Amount should be a number.")
        
        return float(value)
    
    @validates("description")
    def validate_description(self, key, value):
        if not value and value == "No value provided.":
            raise AssertionError("Description should not be empty.")
        return value.strip()

# add the table to dadtabase
# Base.metadata.create_all(engine)