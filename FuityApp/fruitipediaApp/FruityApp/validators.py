
def only_alphabetic(value):
	for char in value:
		if not char.isalpha():
			return False
	return True


