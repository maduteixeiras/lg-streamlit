#crie um programa que solicite ao usuario seu login e uma senha 
# o programa deve continuar pedindo o login e a senha ate que ambos estevam corretos 

import streamlit as st 
st.title("Login")

usuario = "madu"
senha = "123" 

st.session_state.setdefault("desativar", False)
st.session_state.setdefault("tentativas", 0)

usuario_2 = st.text_input("Usuário" , disabled= st.session_state.desativar)
senha_2 = st.text_input("Senha", type="password", disabled= st.session_state.desativar)

if st.button("entrar"):
    if usuario_2 == usuario and senha_2 == senha:
        st.success("senha e login válidos") 
    else: 
        st.session_state.tentativas += 1
        if st.session_state.tentativas <= 3:
            st.warning("login ou senha inválidos. Após 3 tentativas será bloquado!")
        else: 
            st.session_state.desativar = True
            st.error("Máximo de tentativas alcançado")



