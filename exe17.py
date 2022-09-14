#crie um program que leia o cateto oposto e o cateto adjacente e calcule e mostre o resultado da hipotenusa
from math import sqrt ,pow
print('='*20)
print('Ache o valor da hipotenusa ')
co = int(input('Digite o valor do Cateto Oposto '))
ca = int(input('Digite o valor do Cateto Adjacente '))
print('O valor do CATETO OPOSTO {}, CATETO ADJACENTE {}, O resultado da Hipotenusa é {:.2f} '.format(co, ca, sqrt (pow (ca,2) + pow (co,2))))
