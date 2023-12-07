from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

from main import engine

Base = declarative_base()


class User(Base):
	__tablename = 'users'

	id = Column(Integer, primary_key=True)
	username = Column(String(255))
	email = Column(String(255))


Base.metadata.create_all(engine)