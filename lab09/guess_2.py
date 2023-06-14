#!/usr/bin/env python3
import random
my_number = random.randrange(1,100)
answer ='y'
while answer == 'y':
    guess = int(input("Enter a number between 1 and 99: "))
    if guess > my_number:
        print(f'Your guess of: {guess} was too high')
    elif guess < my_number:
        print(f'Your guess of: {guess} was too low')
    else:
        print(f'Your guess of: {guess} was correct!!')
        break
    answer = input('Do you want another guess? y/n: ').lower()