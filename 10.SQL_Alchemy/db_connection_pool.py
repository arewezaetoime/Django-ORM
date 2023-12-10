from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from main import engine
from models import User

# Create a session factory
Session = sessionmaker(bind=engine)
# Use sessions as needed


with Session as session:
	actual_users = session.query(User).all()
	if actual_users:
		for user in actual_users:
			print(f'User: {user.id}')

# Close the session
session.close()