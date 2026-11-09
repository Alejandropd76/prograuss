import streamlit as st

st.sidebar.header("Mi primera barra lateral de Streamlit")
st.sidebar.subheader("¡Hola, Alejandro!")
st.sidebar.write("Esto es una barra lateral")

st.sidebar.image("logo_uss.png", use_container_width=True)

st.sidebar.button("Haz clic en la barra lateral")

texto_ingresado = st.sidebar.text_input("Escribe una palabra:")
st.sidebar.write(f"Escribiste: {texto_ingresado}")

st.header("Mi primera aplicación de Streamlit")
st.subheader("¡Hola, Alejandro!")

texto_principal = st.text_input("Escribe algo:")


st.image("logo_uss.png", use_container_width=True)


