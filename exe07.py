# fazer um programa com a medias das notas de alunos
nome = input('Olá Aluno qual seu nome? ')
print('É um prazer aluno {}, agora para calcular sua media preciso saber os valores'.format(nome))
p1 = float(input('Qual sua primeira nota? '))
p2 = float(input('Qual sua segunda nota? '))
med = (p1 + p2) / 2
print(nome , 'Sua media foi {:.2f}'.format(med))
