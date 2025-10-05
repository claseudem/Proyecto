import streamlit as st

st.title("Menu Principal")

# Crear 5 columnas para los botones
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button("Página 1"):
        st.switch_page("pages/pagina1.py")

with col2:
    if st.button("Página 2"):
        st.switch_page("pages/pagina2.py")

with col3:
    if st.button("Información"):
        st.switch_page("pages/Informacion.py")

with col4:
    if st.button("Analisis"):
        st.switch_page("pages/analisis.py")

with col5:
    if st.button("Graficos"):
        st.switch_page("pages/graficos.py")