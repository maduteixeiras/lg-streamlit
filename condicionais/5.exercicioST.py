#Escrever um programa de computador que solicite do usuário 4 notas e, ao final, apresente a média

import streamlit as st 
st.title("Média")

nota1 = st.number_input("Digite sua 1° nota : \n")
nota2 = st.number_input("Digite sua 2° nota : \n")
nota3 = st.number_input("Digite sua 3° nota : \n")
nota4  = st.number_input("Digite sua 4° nota : \n")

media = (nota1 + nota2 + nota3 + nota4 ) / 4

if st.button("calcular média"):
    st.success(f"Média : {media} ")