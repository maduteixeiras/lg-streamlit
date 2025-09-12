
#Escrever um programa de computador que solicite do usuário 5 números inteiros e, 
# ao final, apresente a soma de todos os números lidos
import streamlit as st 
st.title("Somar")

QUANTIDADE_NUM = 5 
soma = 0 

for i in range (QUANTIDADE_NUM): 
    num = st.number_input(f"Digite o {i + 1}° valor : ", step=1)
    soma = soma + num 

if st.button("somar valores"):
    st.success(f"Resultado = {soma}")