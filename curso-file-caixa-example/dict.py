cars = {}

cars['a'] = '1'
cars['b'] = '2'
cars['c'] = '3'

print(cars.items())

for item in cars:
    print(item + " = " + cars[item])

for key, value in cars.items():
    print(key + " = " + value)
