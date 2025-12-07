import csv
from PhoneNumberLinter import validate_and_format_phone_number
from EmailLinter import validate_and_report_email



def print_contacts_from_csv(filename):
	"""
	Reads a CSV file where each row contains four comma-separated values:
	first name, last name, email, phone number. Prints those values for each row.

	Args:
		filename (str): path to the CSV file
	"""
	try:
		with open(filename, newline='', encoding='utf-8') as csvfile:
			reader = csv.reader(csvfile)
			for row in reader:
				# Skip empty rows
				if not row:
					continue

				# If there are more than four columns, take the first four.
				# If fewer, pad with empty strings so unpacking doesn't fail.
				padded = (row + [""] * 4)[:4]
				first_name, last_name, email, phone = padded
				cleanPhoneNumber = validate_and_format_phone_number(phone)
				cleanEmail = validate_and_report_email(email)
				print(f"First name: {first_name},\nLast name: {last_name},\nCleanEmail: {cleanEmail},\nEmail: {email},\nPhone: {cleanPhoneNumber},\nPhone: {phone}")
				print('-' * 40)
	except FileNotFoundError:
		print(f"File not found: {filename}")
	except Exception as e:
		print(f"Error reading '{filename}': {e}")


if __name__ == '__main__':
	# default file name from workspace
	print_contacts_from_csv('Data Cleaning Prompt - Sheet1.csv')

