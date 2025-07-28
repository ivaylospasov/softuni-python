import io
import sys
from contextlib import redirect_stdout
import importlib.util

# Import the Email class from the email.py file
spec = importlib.util.spec_from_file_location("email_module", "C:/Users/i_spa/PycharmProjects/softuni-python/02 PYTHON FUNDAMENTALS/06 Objects and Classes/01 Lab/email.py")
email_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(email_module)
Email = email_module.Email

# Test input
test_input = """Peter John Hi,John
John Peter Hi,Peter!
Katy Lilly Hello,Lilly
Stop
0, 2"""

# Expected output
expected_output = """Peter says to John: Hi,John. Sent: True
John says to Peter: Hi,Peter!. Sent: False
Katy says to Lilly: Hello,Lilly. Sent: True
"""

# Redirect stdin to use our test input
sys.stdin = io.StringIO(test_input)

# Capture stdout to compare with expected output
f = io.StringIO()
with redirect_stdout(f):
    # Create a list to store Email objects
    emails = []

    while True:
        command = input()
        
        if command == "Stop":
            break
        
        sender, receiver, content = command.split(" ", 2)
        email = Email(sender, receiver, content)
        emails.append(email)

    indices = input().split(", ")
    indices = [int(index) for index in indices]

    for index in indices:
        emails[index].send()

    for email in emails:
        print(email.get_info())

# Get the captured output
actual_output = f.getvalue()

# Compare actual output with expected output
print("Test passed:", actual_output == expected_output)
print("\nActual output:")
print(actual_output)
print("\nExpected output:")
print(expected_output)