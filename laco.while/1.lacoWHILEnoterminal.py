# solicitar nota do aluno caso menor que 0 ou maior que 10 mostre a pergunta novamente 
#mostre a nota do usurio 
import os 
os.system("cls")

while True: 
    nota = float(input("Digite sua nota \n"))
    if nota >= 0 and nota <= 10:
        print("\nNota aceita")
        break
    else:
        print("\nNota invalida ")


