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

# Exercise 2

float_one_ceil = math.ceil(float_one)

# Exercise 3

float_one_sqrt = math.sqrt(float_one_ceil)

# Exercise 4

dict_player_one = dict_players['6']

# Exercise 5

# Una forma

level= tupla_book[0] # Lo selecciono como hago con la lista

print(level)

# Otra forma

one_level, two_author, three_title = tupla_book # empaqueto los elementos de la tupla 

print(one_level) # puedo hacer lo que necesite con él primer elemento como puede ser imprimir

# Exercise 6

list_name.append('Casandra')

# Exercise 7

list_name[0] = 'Jokin'



