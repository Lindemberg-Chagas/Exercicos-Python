#Crie um programa que mostre o dobro, triplo é a raiz quadrada

n = float(input('Digite o valor '))
do = n * 2
tri = n * 3
rz = n ** (1/2)

print('O valor digitado foi {:1}, seu dobro é {:1} e seu triplo é {:1} a Raiz quadrada é {:.2f} '.format( n ,do ,tri , rz ))