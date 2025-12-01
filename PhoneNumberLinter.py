import re

valid_numbers = []
invalid_numbers = []

def validate_and_format_phone_number(phonenumber):
    # Strip whitespace and skip empty lines or comments
    line = phonenumber.strip()
    if not line or line.startswith('#'):
        return
                
         # Extract only digits from the phone number
    digits = re.sub(r'\D', '', line)

         # Check if the number has exactly 10 digits
    if len(digits) == 10:
         # Format as XXX-XXX-XXXX
        formatted_number = f"{digits[0:3]}-{digits[3:6]}-{digits[6:10]}"
        valid_numbers.append(formatted_number)
        return formatted_number
    else:
            # Keep the original format for invalid numbers
        invalid_numbers.append(line)
        return "xxx-xxx-xxxx"

def validate_and_format_phone_numbers(filename):
    """
    Reads phone numbers from a file, validates them, and formats valid ones.
    
    Valid phone numbers must have exactly 10 digits.
    Valid numbers are formatted as: XXX-XXX-XXXX
    
    Args:
        filename (str): Path to the file containing phone numbers
    """
    try:
        with open(filename, 'r') as file:
            for line in file:
                validate_and_format_phone_number(line)
        
        # Print the results
        print("=" * 50)
        print("VALID PHONE NUMBERS:")
        print("=" * 50)
        if valid_numbers:
            for number in valid_numbers:
                print(number)
        else:
            print("No valid phone numbers found.")
        
        print("\n" + "=" * 50)
        print("INVALID PHONE NUMBERS:")
        print("=" * 50)
        if invalid_numbers:
            for number in invalid_numbers:
                print(number)
        else:
            print("No invalid phone numbers found.")
        
        print("\n" + "=" * 50)
        print(f"Summary: {len(valid_numbers)} valid, {len(invalid_numbers)} invalid")
        print("=" * 50)
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: {e}")

# Main execution
if __name__ == "__main__":
    validate_and_format_phone_numbers("PhoneNumbers.txt")
