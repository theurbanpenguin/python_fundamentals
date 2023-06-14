#!/usr/bin/env python3
# Simple hard coded number that will be randomized later
my_number = 37
guess = int(input("Enter a number as a guess: "))
if guess > my_number:
    print(f'Your guess of: {guess} was too high')
elif guess < my_number:
    print(f'Your guess of: {guess} was too low')
else:
    print(f'Your guess of: {guess} was correct!!')

