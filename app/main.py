import os
import yaml

def phone_book_exists():
	""" 
	this function checks for phone_book.yml,
	if it is present returns True,
	if not present returns False
	"""
	phone_book_exists = os.path.isfile('phone_book.yml')
	return phone_book_exists


def create_phone_book():
	"""
	this function creates phone_book.yml file
	"""
	initial_dict = {'phone_book': []}
	with open("phone_book.yml", "w") as f:
		yaml.dump(initial_dict, f)

def get_phone_book():
	pass

def ask_information():
	pass

def add_to_phonebook(new_record=None):
	pass

if __name__ == '__main__':
	if not phone_book_exists():
		create_phone_book()
	else:
		phone_book = get_phone_book()
		new_record = ask_information()
		add_to_phonebook(new_record)
		print('Contact successfully Added')