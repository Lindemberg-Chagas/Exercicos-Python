#crie um programa que liste o nome dos alunos em sequencia
print('='*50)
print('Escolher sequencia de alunos da apresentação')
print('='*50)
from random import shuffle
al1 = input('Digite o primeiro nome ')
al2 = input('Digite o segundo nome ')
al3 = input('Diigte o terceiro nome ')
al4 = input('Digite o quarto nome ')
seq = [al1, al2, al3, al4 ]
shuffle(seq)
print(seq)

