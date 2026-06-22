import streamlit as st
import requests as r

# # be_server_url = "http://localhost:8000"
# be_server_url="https://rolebasedproject.onrender.com"
be_server_url=st.secrets("be_server_url")

st.title("Job Seeker Dashboard")

menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "View Details",
        "Apply Job",
        "View Applied Status"
    ]
)

if menu == "View Details":

    st.header("Current Openings")

    st.write("Python Developer")
    st.write("Java Developer")
    st.write("Data Analyst")
    st.write("Frontend Developer")
    st.write("Backend Developer")

elif menu == "Apply Job":

    st.header("Apply Job")

    email = st.text_input("Email")

    job_role = st.selectbox(
        "Select Job Role",
        [
            "Python Developer",
            "Java Developer",
            "Data Analyst",
            "Frontend Developer",
            "Backend Developer"
        ]
    )

    if st.button("Apply"):

        payload = {
            "email": email,
            "job_role": job_role
        }

        res = r.post(
            f"{be_server_url}/apply_job",
            json=payload
        )

        st.write(res.json())

elif menu == "View Applied Status":

    st.header("Applied Status")

    email = st.text_input("Enter Email")

    if st.button("View"):

        res = r.get(
            f"{be_server_url}/view_applied_details/{email}"
        )

        data = res.json()

        for row in data:

            st.write(
                "Email :",
                row["email"]
            )

            st.write(
                "Role :",
                row["job_role"]
            )

            st.write(
                "Status :",
                row["status"]
            )

            st.divider()