# SOLICITAR 2 NOTAS PRO ALUNO QUE SEJAM ENTRE 0 E 10 
#SE NÃO FOREM PERGUNTA A NOTA DE NOVO 
# SE AS NOTAS FOREM VÁLIDAS MOSTRA A MÉDIA DO ALUNO 


import streamlit as st 
st.title("Laço de Repetição - While em Streamlit")

QUANTIDADE_NOTAS = 2
notas = []
soma = 0 


for i in range(QUANTIDADE_NOTAS):
    notas = st.number_input(f"Digite sua {i+1}° nota:", min_value=0 , max_value=10) 

if st.button("visualizar média"):
    soma = soma + notas 
    media = soma /2 
    st.info(f"Média = {media}")





