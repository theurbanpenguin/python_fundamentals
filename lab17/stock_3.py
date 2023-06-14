import yaml
import os

file = 'my.yaml'

# Let's check if the file exists
# If it doesn't create an empty stock dictionary
# If it does exist we read the YAML into stock dictionary
if not os.path.exists(file):
    stock = {}
else:
    with open(file, 'r') as f:
        stock = yaml.safe_load(f)

answer = 'y'

while answer == 'y':
    stock_number = len(stock) + 1
    make = input("Enter a make: ")
    model = input("Enter a model: ")

    stock[stock_number] = {}
    stock[stock_number]['make'] = make
    stock[stock_number]['model'] = model

    print(yaml.dump(stock))
    answer = input("Do you want to add another car? y/n: ")

with open(file, 'w') as f:
    print(yaml.dump(stock), file=f)


