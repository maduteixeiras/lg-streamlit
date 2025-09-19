#Construa um algoritmo que calcule a média aritmética de vários valores inteiros positivos, inseridos pelo usuário. 
#O final da leitura acontecerá quando for lido um valor negativo.
#Mostre a média aritmética dos números informados pelo usuário.
import os 
os.system("cls")

quant_valores = 0 
soma = 0 

while True: 
    valor = float(input("Insira um valor:\n"))
    if valor < 0: 
        break
    quant_valores += 1
    soma += valor
    media = soma / quant_valores

print(f"Sua média foi {media}")



    