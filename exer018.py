#Faça um programa que leia o angulo e retone o valor do Seno, Coseno e Tangente
print('-'*50)
print('DIGITE O ANGULO QUE MOSTRO OS VALORES DE SENO, COSSENO E TANGENTE')
from math import cos, sin, tan, radians
an = int(input('Digite o angulo '))
ra = radians(an)
print('Para o Angulo de {}° , o Seno dele vale {:.4f}, o Cosseno Vale {:.4f} e a Tangente vale {:.4f}'.format(an, sin(ra), cos(ra), tan(ra)))