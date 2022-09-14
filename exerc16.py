#Crie um programa que leia uma valor Real e mostre apenas o valor inteiro
from math import trunc
num = float(input('Digite uma valor '))
print('O numero digitado foi {} e o valor inteiro é {} '.format(num,trunc(num)))
