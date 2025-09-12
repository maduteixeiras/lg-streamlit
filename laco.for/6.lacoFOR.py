#Escreva um algoritmo que solicite ao usuário 5 valores
#inteiros e ao final mostre: 
# quantos números são pares; 
#quantos números são ímpares;

import streamlit as st 
st.title("Impar Ou par")

num1 = st.number_input(f"Digite o 1° número : ", step=1)
num2 = st.number_input(f"Digite o 2° número : ", step=1)
num3 = st.number_input(f"Digite o 3° número : ", step=1)
num4 = st.number_input(f"Digite o 4° número : ", step=1)
num5 = st.number_input(f"Digite o 5° número : ", step=1)

if st.button("confirmar"):
    num_pares = 0 
    num_impar = 0 
    
    for i in [num1, num2, num3, num4, num5]:
        if i % 2 == 0:
            num_pares = num_pares + 1
        else:
            num_impar = num_impar + 1
    st.success(f"{num_pares} desses números são PAR")
    st.success(f"{num_impar} desses números são IMPAR")

    


