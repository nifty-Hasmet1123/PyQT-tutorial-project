# from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey
# from sqlalchemy.orm import declarative_base, relationship
# from datetime import datetime

# from .db import engine

# Reference: https://coderpad.io/blog/development/sqlalchemy-with-postgresql/

# automatically fill out the init
# Base = declarative_base()

# class Article(Base):
#     __tablename__ = "articles"

#     id = Column(Integer(), primary_key=True)
#     slug = Column(String(100), nullable=False, unique=True)
#     title = Column(String(100), nullable=False)
#     created_on = Column(DateTime(), default=datetime.now)
#     updated_on = Column(DateTime(), default=datetime.now, onupdate=datetime.now)
#     content = Column(Text)
#     author_id = Column(Integer(), ForeignKey('authors.id'))


# class Author(Base):
#     __tablename__ = "authors"

#     id = Column(Integer(), primary_key=True)
#     firstname = Column(String(100))
#     lastname = Column(String(100))
#     email = Column(String(255), nullable=False)
#     joined = Column(DateTime(), default=datetime.now)

#     articles = relationship('Article', backref='author') # creates a brand new column called author in the Article class

#     # customize column
#     full_name = Column(String(255)) # customize column

#     def __init__(self, firstname, lastname, email, **kwargs):
#         super().__init__(**kwargs)
#         self.firstname = firstname
#         self.lastname = lastname
#         self.email = email
#         self.full_name = f"{firstname} {lastname}"



### add the two tables within database using this code
# Base.metadata.drop_all(engine)
# Base.metadata.create_all(engine)
