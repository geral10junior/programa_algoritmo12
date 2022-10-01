#A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo.

numero= int(input("informe o número: "))
numero_atual= 1
numero_antecessor= 0
numero_temporario= 0

for i in range(numero):
    numero_temporario= numero_atual
    print(numero_temporario)
    numero_atual= numero_atual + numero_antecessor
    numero_antecessor= numero_temporario

