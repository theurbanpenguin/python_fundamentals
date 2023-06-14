#!/usr/bin/env python3
temp_fahrenheit = int(input('Enter a temperature in fahrenheit: '))
temp_centigrade = (temp_fahrenheit - 32) / 1.8
print(f'{temp_centigrade:.2f}')