#!/usr/bin/env python3
from sys import argv
import mymodule

file = mymodule.basename(argv[0])

try:
    email = argv[1]
except IndexError:
    email = input(f'Script {file} needs an email: ')

finally:
    e = mymodule.split_email(email)
    print("User: " + e['user'])
    print("Domain: " + e['domain'])
