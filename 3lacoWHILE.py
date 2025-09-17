
#crie um programa que solicite ao usuario seu login e uma senha 
# o programa deve continuar pedindo o login e a senha ate que ambos estevam corretos 
# maxi de tentativas de 3x 
import os 
os.system("cls")

usuario = "madu"
senha = "123"

tentativas = 0
maxtentativas = 3 

while tentativas < maxtentativas :
    usuario_2 = str(input("Digite seu suário: \n"))
    senha_2 = str(input("Digite sua senha \n"))
    tentativas += 1
    if usuario_2 == usuario and senha_2 == senha:
        print("\nSenha e login válidos")
        break
    else: 
        if tentativas == maxtentativas: 
            print("bloqueado por muitas tentativa")
        else: 
            print("\nTente novamente. Após 3 tentativas será bloquado!")
