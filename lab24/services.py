import re

file = '/etc/services'

with open(file, 'r') as f:
    expression = '^http\s'
    matching_lines = [line for line in f if re.search(expression, line)]
    print(''.join(matching_lines))
