from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from main import engine

Base = declarative_base()


class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	username = Column(String(255))
	email = Column(String(255))


class Order(Base):
	__tablename__ = 'orders'

	id = Column(Integer, primary_key=True)
	is_completed = Column(Boolean, default=False)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

	user = relationship('User')


Base.metadata.create_all(engine)