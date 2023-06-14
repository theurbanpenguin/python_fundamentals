import yaml

cars = {}
cars[1] = {'make': 'ford', 'model': 'f150'}
cars[2] = {'make': 'ford', 'model': 'f100'}
cars[3] = {'make': 'ford', 'model': 'bronco'}

print(yaml.dump(cars))
