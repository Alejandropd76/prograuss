import streamlit as st

# ==========================================
# 1. BARRA LATERAL (SIDEBAR)
# ==========================================
st.sidebar.header("Mi primera barra lateral de Streamlit")
st.sidebar.write("¡Hola, Barra Lateral!")

# Imagen de la universidad en la barra lateral
st.sidebar.image("logo_uss.png", use_container_width=True)

# Componentes interactivos de la barra lateral
st.sidebar.checkbox("Haz clic en esta casilla")
st.sidebar.radio("Elige una opción:", ["Opción 1", "Opción 2"])

# Entrada de texto (guardamos lo que el usuario escribe en una variable)
texto_ingresado = st.sidebar.text_input("Escribe una palabra:")


# ==========================================
# 2. ÁREA PRINCIPAL (MAIN)
# ==========================================
st.header("Mi primera aplicación de Streamlit")
st.write("¡Hola, Streamlit!")

# Salida del texto ingresado en la barra lateral
st.write(f"Escribiste: {texto_ingresado}")

# Imagen de la universidad en el área principal
st.image("logo_uss.png", use_container_width=True)
