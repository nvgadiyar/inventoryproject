import re


def validate_and_report_emails(filename):
	"""
	Reads email addresses from a file and prints two lists:
	- valid emails (those that match a reasonable email regex)
	- invalid emails (anything that doesn't match)

	The function skips blank lines and lines that start with '#' (comments).

	Args:
		filename (str): path to a text file containing one email per line
	"""
	# A reasonably strict, practical email regex:
	#  - local part: letters, digits and a few punctuation characters
	#  - single @
	#  - domain: labels of letters/digits/hyphen separated by single dots
	#  - final TLD is alphabetic and at least 2 characters
	email_re = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}$", re.IGNORECASE)

	valid = []
	invalid = []

	try:
		with open(filename, 'r', encoding='utf-8') as f:
			for raw in f:
				line = raw.strip()
				if not line or line.startswith('#'):
					continue

				# Normalize common problems before validating:
				# 1) Remove spaces immediately before or after '@' and '.' characters
				#    so 'chloe.lopez@ example .com' => 'chloe.lopez@example.com'.
				# 2) In the domain part, convert commas to dots and collapse repeated
				#    dots (example..com => example.com). This fixes common formatting
				#    errors while avoiding aggressive changes to the local part.
				candidate = re.sub(r'(?<=[@.])\s+|\s+(?=[@.])', '', line)

				# If there's exactly one '@', apply domain-specific normalizations
				if candidate.count('@') == 1:
					local_part, domain_part = candidate.split('@', 1)

					# replace commas with dots in domain and collapse consecutive dots
					domain_fixed = domain_part.replace(',', '.')
					domain_fixed = re.sub(r'\.{2,}', '.', domain_fixed)

					candidate = f"{local_part}@{domain_fixed}"

				# If normalization changed the string, validate the fixed one;
				# otherwise validate the original trimmed input.
				to_check = candidate if candidate != line else line

				if email_re.fullmatch(to_check):
					# Append the normalized form so valid outputs are clean
					valid.append(to_check)
				else:
					invalid.append(line)

		# Print results
		print('=' * 70)
		print('VALID EMAILS:')
		print('=' * 70)
		if valid:
			for e in valid:
				print(e)
		else:
			print('No valid emails found.')

		print('\n' + '=' * 70)
		print('INVALID EMAILS:')
		print('=' * 70)
		if invalid:
			for e in invalid:
				print(e)
		else:
			print('No invalid emails found.')

		print('\n' + '=' * 70)
		print(f'Summary: {len(valid)} valid, {len(invalid)} invalid')
		print('=' * 70)

	except FileNotFoundError:
		print(f"File not found: {filename}")


if __name__ == '__main__':
	# Default runtime when executed directly
	validate_and_report_emails('Email.txt')

