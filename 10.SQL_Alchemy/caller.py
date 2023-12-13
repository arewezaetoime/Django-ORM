from sqlalchemy.orm import sessionmaker

from Exercise.models_ex import Recipe
from helper import session_decorator
from main import engine
from models import User, Order

Session = sessionmaker(bind=engine)
session = Session()

# with Session() as session:
# 	new_user = User(username='Gosho', email='gosho@localhost.com')
# 	session.add(new_user)
# 	session.commit()
#
# with Session() as session:
# 	users = session.query(User).all()
#
# 	for u in users:
# 		print(u.username, u.email)
#
# with Session() as session:
# 	user_to_update = session.query(User).filter_by(username='Gosho').first()
#
# 	if user_to_update:
# 		user_to_update.email = 'goshoto@geshka.bg'
# 		session.commit()
# 		print('Email updated successfully')
# 	else:
# 		print('Email update was unsuccessful')
#
# with Session() as session:
# 	user_to_delete = session.query(User).filter_by(username='Gosho').first()
#
# 	if user_to_delete:
# 		session.delete(user_to_delete)
# 		session.commit()
# 		print(f'{user_to_delete.username} was deleted successfully')
# 	else:
# 		print(f'{user_to_delete.username} was not deleted')


def populate_order_table():
	with Session() as session:
		session.add_all((Order(user_id=5), Order(user_id=3)))
		session.commit()


# populate_order_table()


def relationship_query():
	with Session() as session:
		orders = session.query(Order).order_by(Order.user_id.desc()).all()

		if not orders:
			print("No orders")
			return

		for o in orders:
			user = o.user
			print(f'Order number {o.id}, Is completed: '
				  f'{o.is_completed}, Username: {user.username}')


# relationship_query()


@session_decorator(session)
def create_recipe(name: str, ingredients: str, instructions: str):
    new_recipe = Recipe(
        name=name,
        ingredients=ingredients,
        instructions=instructions
    )

    session.add(new_recipe)