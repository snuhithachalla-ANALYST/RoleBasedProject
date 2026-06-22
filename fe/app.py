import streamlit as st

st.title("Job Portal")

col1, col2 = st.columns(2)

with col1:
    if st.button("Register"):
        st.switch_page("pages/register.py")

with col2:
    if st.button("Login"):
        st.switch_page("pages/login.py")