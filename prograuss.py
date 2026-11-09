import streamlit as st

st.sidebar.header("Mi primera barra lateral de Streamlit")
st.sidebar.write("¡Hola, Barra Lateral!")

st.sidebar.image("logo_uss.png", use_container_width=True)

st.sidebar.checkbox("Haz clic en esta casilla")

texto_ingresado = st.sidebar.text_input("Escribe una palabra:")

st.header("Mi primera aplicación de Streamlit")
st.write("¡Hola, Streamlit!")

# Imagen de la universidad en el área principal
st.image("logo_uss.png", use_container_width=True)
st.text_input = st.write(f"Escribiste: {texto_ingresado}")

