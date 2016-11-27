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
		yaml.dump(initial_dict, f, default_flow_style=False)
	print('phone book created successfully')

def get_phone_book():
	"""
	Reads phone_book.yml and creates phone_book dictionary
	"""
	with open("phone_book.yml", "r") as f:
		phone_book = yaml.load(f)
	return phone_book

def ask_information():
	"""
	ask user for dynamic input and creates new_record dict
	"""
	first_name = "vishnu"
	last_name = "vardhan"
	phone_number = "9666021667"
	email = "vishnu.narpala@gmail.com"
	new_record = {
		"first_name": first_name,
		"last_name": last_name,
		"phone_number": phone_number,
		"email": email,
	}
	return new_record


def add_to_phonebook(phone_book=None, new_record=None):
	"""
	This function takes previous phone_book dict and new_record
	appends new_record to phone_book dict
	writes updated phone_book dict to phone_book.yml
	"""
	phone_book['phone_book'].append(new_record)
	with open("phone_book.yml", "w") as f:
		yaml.dump(phone_book, f, default_flow_style=False)

if __name__ == '__main__':
	if not phone_book_exists():
		create_phone_book()
	else:
		new_record = ask_information()
		phone_book = get_phone_book()
		add_to_phonebook(phone_book, new_record)
		print('Contact successfully Added')