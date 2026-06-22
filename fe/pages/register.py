import streamlit as st
import requests as r

# be_server_url = "http://localhost:8000"
be_server_url="https://rolebasedproject.onrender.com"

st.title("Register")

with st.form("RegisterForm"):

    n = st.text_input("Name")
    e = st.text_input("Email")
    p = st.text_input("Password", type="password")
    c = st.text_input("Confirm Password", type="password")

    role = st.selectbox(
        "Choose Role",
        ["recruiter", "job seeker"]
    )

    register_btn = st.form_submit_button("Register")

    if register_btn:

        payload = {
            "name": n,
            "email": e,
            "password": p,
            "confirm_password": c,
            "role": role
        }

        res = r.post(
            f"{be_server_url}/register",
            json=payload
        )

        st.write(res.text)