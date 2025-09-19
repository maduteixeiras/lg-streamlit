#Escreva um algoritmo que pergunte ao usuário se deseja inserir
#mais uma nota, 
#se a resposta do usuário for “N”, 
#o programa fará a média aritmética das notas informadas 
#e mostrará a média aritmética para o usuário.
# Obs.: Use um contador dentro do laço de repetição para contar a
# quantidade de iterações (loops).


import os 
os.system("cls")

nota1 = float(input("Insira sua primeira nota:\n"))
nota2 = float(input("Insira sua segunda nota:\n"))

while True: 
    opcap_inserir = input("Deseja inserir mais uma nota? \nselecione 'S' caso Sim  \nselecione 'N' caso Não \n").upper()
    if opcap_inserir == "N" or opcap_inserir == "S":
        break

match opcap_inserir: 
    case "N": 
        print(f"\n{(nota1 + nota2) / 2} foi sua média")
    case "S": 
        nota3 = float(input("\nInsira sua terceira nota:\n"))
        print(f"\n{(nota1 + nota2 + nota3) / 3} foi sua média")
    case _: 
        print("""
selecione 'S' caso Sim"
selecione 'N' caso Não9
        """)
