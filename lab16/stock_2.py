import yaml

answer = 'y'
stock = {}

while answer == 'y':
    stock_number = len(stock) + 1
    make = input("Enter a make: ")
    model = input("Enter a model: ")

    stock[stock_number] = {}
    stock[stock_number]['make'] = make
    stock[stock_number]['model'] = model

    print(yaml.dump(stock))

    answer = input("Do you want to add another car? y/n: ")
