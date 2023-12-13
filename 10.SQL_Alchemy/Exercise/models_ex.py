from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship

from models import Base


class Recipe(Base):
	__tablename__ = 'recipes'

	id = Column(Integer, primary_key=True, unique=True, nullable=False,)
	name = Column(String, nullable=False, blank=False,)
	ingredients = Column(Text, nullable=False, blank=False,)
	instructions = Column(Text, nullable=False, blank=False,)


class Chef(Base):
	__tablename__ = 'chefs'

	id = Column(Integer, primary_key=True,)
	name = Column(String(100), nullable=False,)

	recipes = relationship("Recipe", back_populates="chef")
