# SOLICITAR 2 NOTAS PRO ALUNO QUE SEJAM ENTRE 0 E 10 
#SE NÃO FOREM PERGUNTA A NOTA DE NOVO 
# SE AS NOTAS FOREM VÁLIDAS MOSTRA A MÉDIA DO ALUNO 


import streamlit as st 
st.title("Laço de Repetição - While em Streamlit")

QUANTIDADE_NOTAS = 2
soma = 0 


for i in range(QUANTIDADE_NOTAS):
    notas = st.number_input(f"Digite sua {i+1}° nota:")
if st.button("verificar"):
    if notas > 10:
        st.error("Notas maior que 10. Não aceitas!")
    elif notas < 0:
        st.error("Notas menor que 0. Não aceitas!")
    else:
        st.success("notas aceitas")

if st.button("visualizar média"):
            soma = soma + notas 
            media = soma /2 
            st.info(f"Média = {media}")
       
       
#TA COM ERRO, CONSERTAR !!!!
        




