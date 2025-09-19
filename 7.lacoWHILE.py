#faça um algoritmo que leia uma quantidade não
#determinada de números inteiros positivos. Calcule: 
#quantidade de números pares e ímpares; 
#média de valores pares 
#média geral dos números lidos. 
#O número que encerrará a leitura será o número zero

import os 
os.system("cls")

soma_pares = 0 
soma_impares = 0 
quantidade_pares = 0 
quantidade_impares = 0 
quantidade_num_total = 0 
print("O programa revela a quantidade de numero impares e pares ao selecionar o númeral 0")

while True: 
    numero = int(input("\nDígite um número:\n "))
    if numero == 0: 
        break

    quantidade_num_total += 1
    if numero % 2 == 0: 
        quantidade_pares += 1
        soma_pares += numero
        media_pares = soma_pares / quantidade_pares
    else: 
        quantidade_impares += 1 
        soma_impares += numero
        media_impares = soma_impares / quantidade_impares
        
    
    print(f"Quantidade de número inseridos: {quantidade_num_total}")
    print(f"Quantidade de números pares: {quantidade_pares}")
    print(f"Média dos números pares: {media_pares}")
    print(f"Quantidade números impares :{quantidade_impares}")
    print(f"Média dos números pares: {media_impares}")



#erro depois resolver

