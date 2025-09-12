#Escrever um programa de computador que solicite do usuário 3 notas e, 
# ao final, apresente a média e mostre para o usuário se o aluno está aprovado, em recuperação ou reprovado. 
#Considere que para aprovação, deve-se obter média maior ou igual a 7, para ser reprovado, a média deve ser menor que 4.

import streamlit as st 
st.title("Boletim Final")

QUANTIDADE_NOTAS = 3
soma = 0

for i in range(QUANTIDADE_NOTAS): 
    nota = st.number_input(f"Digite a {i+1}° nota : ")
    soma = (soma + nota)
    media = soma /3 

if st.button("revelar média"):
    st.info(f"Média: {media}")

if st.button("revelar resultado final"):
    if media >= 7: 
        st.success("Parabéns! Você foi aprovado.")
    elif media < 4: 
        st.error("Infelizmente você foi reprovado :(")
    else: 
        st.warning("Você está na recuperação : /")