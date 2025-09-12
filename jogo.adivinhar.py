#criar um jogo que de ao usuario 5 chances de acertar um numero 

import os
os.system("cls")
import random 


num_correto = random.randint(1,20)
tentativas = 0 
tentativas_max = 5

print (f"{num_correto}")

while tentativas < tentativas_max:
    chute_user = int(input("Adivinhe o número\n"))
    tentativas = tentativas + 1
    if num_correto == chute_user:
        print(f"Parabéns!! Você acertou o número com {tentativas} tentativas")
        break
    else:
        if tentativas == tentativas_max:
            print(f"Suas {tentativas_max} tentativas acabaram. O número correto era {num_correto}.")
        else:
            print("Tente novamente!")