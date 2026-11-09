import streamlit as st

st.image("logo_uss.png", use_container_width=True)

texto_principal = st.text_area("Escribe algo:")
st.write(f"Escribiste_esto: {texto_principal}")

st.sidebar.header("Mi primera barra lateral de Streamlit")
st.sidebar.subheader("¡Hola, Alejandro!")
st.sidebar.write("Esto es una barra lateral")

st.sidebar.image("logo_uss.png", use_container_width=True)

st.sidebar.button("Haz clic en la barra lateral")

texto_ingresado = st.sidebar.text_input("Escribe una palabra:")
st.sidebar.write(f"Escribiste: {texto_ingresado}")
