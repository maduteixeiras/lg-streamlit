#Faça um algoritmo que mostre um menu com
#pções de um cardápio de restaurante para
#uma pessoa. A pessoa vai escolher o prato
#desejado.
#Calcule quanto deve ser pago pelo cliente

import streamlit as st
from PIL import Image
# instala com  = pip install streamlit Pillow

st.title("Cardápio Virtual")
img = Image.open('tabela.png')
# link da imagem google = https://share.google/images/dg2N2PbAdQkYTlRVo
st.image(img, caption="valores e produtos")
#mercadorias = ["Café",    "Açucar",     "Bolacha",     "Sal" ]
#precos =     [ 5.00 ,      2.00 ,         8.00 ,       3.00]

mercadorias = st.selectbox(
    "Qual mercadoria você deseja?",
    ["Café", "Açúcar", "Bolacha", "Sal"]
)

match mercadorias:
    case "Café" : 
        preco = 5.00
    case "Açúcar": 
        preco = 2.00
    case "Bolacha": 
        preco = 8.00
    case "Sal": 
        preco = 3.00

if st.button("Valor dos produtos"):
    st.success(f"{preco}$")