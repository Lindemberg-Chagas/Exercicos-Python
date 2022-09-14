# faça um programa que ajude um professor a escolher um dos quatros alunos para apagar o quadro
import random

print('-' * 50)
print('sorteio de quem vai apagar o quadro')
alu1 = input('Digite o nome do primeiro Aluno ')
alu2 = input('Digite o nome do segundo Aluno ')
alu3 = input('Digite o nome do Terceiro Aluno ')
alu4 = input('Digite o nome do Quarto Aluno ')
seq = (alu1, alu2, alu3, alu4)
print('O nome dos canditadados a apagar o quadrao são {} , {} , {} e {} '.format(alu1, alu2, alu3, alu4))
print('E o nome escolhido é...tchan...tchan...tchan...')
print(random.choice(seq))
