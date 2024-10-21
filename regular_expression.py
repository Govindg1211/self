import re

text = """
Contact us at support@example.com or call us at (123) 456-7890.
You can also reach out to sales@example.org for inquiries.
"""

# Example 1: Finding all email addresses in the text
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
emails = re.findall(email_pattern, text)
print("Email addresses found:", emails)
# Output: Email addresses found: ['support@example.com', 'sales@example.org']

# Example 2: Finding all phone numbers in the text
phone_pattern = r'\(\d{3}\) \d{3}-\d{4}'
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)
# Output: Phone numbers found: ['(123) 456-7890']

# Example 3: Searching for a specific pattern
search_pattern = r'support'
match = re.search(search_pattern, text)
if match:
    print(f"Found '{search_pattern}' at position:", match.start())
else:
    print(f"'{search_pattern}' not found.")

# Example 4: Replacing email domains
updated_text = re.sub(r'@example\.com', '@newdomain.com', text)
print("Updated text:\n", updated_text)

# Example 5: Validating a simple email format
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

# Testing the validation function
test_emails = ['test@example.com', 'invalid-email', 'user@domain']
for email in test_emails:
    print(f"Is '{email}' a valid email? {is_valid_email(email)}")