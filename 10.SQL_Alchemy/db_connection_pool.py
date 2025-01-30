from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import engine
from models import User

Session = sessionmaker(bind=engine)

with Session as session:
    users = session.query(User).all()
	
    print(*(f'User: {user.id}' for user in users), sep='\n') if users else None

session.close()
