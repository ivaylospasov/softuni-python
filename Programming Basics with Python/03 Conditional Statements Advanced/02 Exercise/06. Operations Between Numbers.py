n1 = int(input())
n2 = int(input())
n_operator = input()

result = 0
output = ''

if n2 == 0 and (n_operator == '/' or n_operator == '%'):
    output = f'Cannot divide {n1} by zero'
elif n_operator == '/':
    result = n1 / n2
    output = f'{n1} / {n2} = {result:.2f}'
elif n_operator == '%':
    result = n1 % n2
    output = f'{n1} % {n2} = {result}'
else:
    if n_operator == '+':
        result = n1 + n2
    elif n_operator == '-':
        result = n1 - n2
    elif n_operator == '*':
        result = n1 * n2
    output = f"{n1} {n_operator} {n2} = {result} " \
             f"- {('even' if result % 2 == 0 else 'odd')}"

print(output)