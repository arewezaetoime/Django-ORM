from caller import Session
from models import User

session = Session()

try:
	# Begin a transaction
	session.begin()

	# Performing some database operations within the transaction
	new_user = User(username='Mosho', email='kokal@localhost.com')
	session.add(new_user)
	session.commit()

	user_to_update = session.query(User).filter_by(username='Mosho').first()

	if user_to_update:
		user_to_update.email = 'kokal@geshka.bg'
		session.commit()
		print(f'''{user_to_update.username}'s email was updated successfully''')
	else:
		print(f'''{user_to_update.username}'s email was not updated successfully''')

		session.commit()
except Exception as e:
	session.rollback()
	print(f'The transaction was not successful, error message {str(e)}')
finally:
	# Close the session
	session.close()
