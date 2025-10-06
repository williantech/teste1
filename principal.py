import streamlit as st

st.title("Semana da Economia")
st.write("Meu apop")

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)
 