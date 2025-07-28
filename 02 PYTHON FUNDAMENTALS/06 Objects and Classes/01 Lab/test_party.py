import io
import sys
from unittest.mock import patch

# Input data from the example
input_data = '''Peter
John
Katy
End'''

# Expected output
expected_output = '''Going: Peter, John, Katy
Total: 3'''

# Redirect stdin to use our test input
with patch('sys.stdin', io.StringIO(input_data)):
    # Capture stdout to compare with expected output
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    # Execute the script
    exec(open('party.py').read())
    
    # Reset stdout
    sys.stdout = sys.__stdout__
    
    # Get the captured output
    actual_output = captured_output.getvalue().strip()
    
    # Compare with expected output
    print('Test result:')
    print(f'Actual output:\n{actual_output}')
    print(f'Expected output:\n{expected_output}')
    print(f'Test passed: {actual_output == expected_output}')