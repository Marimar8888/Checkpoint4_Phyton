from decimal import Decimal
import math

# Exercise 1

list_name = ['Maria', 'Sara', 'Luis', 'Alberto', 'Lidia']

tupla_book = ('English Intermediate', 'John Milne', 'The Queen')

float_one = 47.20

int_one = 22

dict_players = {
    '6': 'LeBron James',
    '8': 'Kobe Bryan',
    '23': 'Michael Jordan',
    '32': 'Magic Johnson',
    '33': 'Larry Bird',
}

service_price = Decimal(12.99)
print(service_price)
# Exercise 2

float_one_ceil = math.ceil(float_one)
print(float_one_ceil)
# Exercise 3

float_one_sqrt = math.sqrt(float_one_ceil)
print(float_one_sqrt)
# Exercise 4

dict_player_one = dict_players['6']
print(dict_player_one)
# Exercise 5

# Una forma

level= tupla_book[0] # Lo selecciono como hago con la lista
print(level)

# Otra forma

one_level, two_author, three_title = tupla_book # empaqueto los elementos de la tupla 
print(one_level) # puedo hacer lo que necesite con él primer elemento como puede ser imprimir

# Exercise 6

list_name.append('Casandra')
print(list_name)

# Exercise 7

list_name[0] = 'Jokin'
print(list_name)

# Exercise 8

#Si solo quiero ordenarla pero no quiero guardar el resultado en una variable

list_name.sort()
print(list_name)

# Si lo que quiero es crear esa lista ordenada para trabajar sobre ella

list_name_ord = sorted(list_name)
print(list_name_ord)

# Exercise 9
print(id(tupla_book)) # 2145913177216

tupla_book += ('Mistery',)
print(tupla_book)

print(id(tupla_book)) # reasigna el id nuevo objeto 2145913371952
