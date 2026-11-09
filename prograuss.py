import streamlit as st

st.sidebar.header("Mi primera barra lateral de Streamlit")
st.sidebar.subheader("¡Hola, Alejandro!")

st.sidebar.image("logo_uss.png", use_container_width=True)

st.sidebar.button("Haz clic en esta casilla")

texto_ingresado = st.sidebar.text_input("Escribe una palabra:")

st.header("Mi primera aplicación de Streamlit")
st.subheader("¡Hola, Alejandro!")

st.image("logo_uss.png", use_container_width=True)
st.write(f"Escribiste: {texto_ingresado}")

