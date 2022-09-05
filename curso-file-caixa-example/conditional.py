from unicodedata import numeric


i = 100

if i > 100:
    print("Maior que 100")
elif i < 100:
    print("Menor que 100")
else:
    print("ops")


list = [2, 4, 5, 5]

for item in list:
    if not item == 2:
        print(item)

number = 1
while number < 10:
    print(number)
    number += 1
else:
    # print("ultimo numero" + number)
    print("ultimo numero")
