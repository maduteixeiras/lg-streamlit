import os 
os.system("cls")

import streamlit as st 
st.title("Laço de Repetição - While em Streamlit")
 
numero = st.number_input("Digite um valor (0 - 10):")
if st.button("verificar"):
    if numero > 10:
        st.error("Número maior que 10. Tente novamente!")
    elif numero < 0:
        st.error("Número menor que 0. Tente Novamente!")
    else: 
        st.success("Número aceito")

