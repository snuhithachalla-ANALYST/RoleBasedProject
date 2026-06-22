import streamlit as st
import requests as r

# be_server_url = "http://localhost:8000"
be_server_url="https://rolebasedproject.onrender.com"

st.title("Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

role = st.selectbox(
    "Choose Role",
    ["recruiter", "job seeker"]
)

if st.button("Login"):

    payload = {
        "email": email,
        "password": password,
        "role": role
    }

    res = r.post(
        f"{be_server_url}/login",
        json=payload
    )

    data = res.json()

    if "role" in data:

        if data["role"] == "recruiter":

            st.switch_page(
                "pages/r_dashboard.py"
            )

        elif data["role"] == "job seeker":

            st.switch_page(
                "pages/j_dashboard.py"
            )

    else:

        st.error(data["msg"])