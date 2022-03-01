#!/usr/bin/env python3

email = 'tux@example.com'
at = email.find('@')
user = email[:at]
domain = email[at + 1:]
print(f'User: {user}')
print(f'Domain: {domain}')

