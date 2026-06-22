import streamlit as st
import requests as r

be_server_url = "http://localhost:8000"

st.title("Recruiter Dashboard")

col1, col2 = st.columns(2)

with col1:
    post_job_btn = st.button("Post Jobs")

with col2:
    view_btn = st.button("View Applications")

# ---------------- POST JOB ----------------

if post_job_btn:

    st.header("Post New Job")

    role = st.text_input("Role")

    description = st.text_area(
        "Job Description"
    )

    salary = st.text_input(
        "Salary"
    )

    skills_required = st.text_input(
        "Skills Required"
    )

    location = st.text_input(
        "Location"
    )

    if st.button("Post"):

        payload = {
            "role": role,
            "description": description,
            "salary": salary,
            "skills_required": skills_required,
            "location": location
        }

        res = r.post(
            f"{be_server_url}/post_job",
            json=payload
        )

        st.write(res.json())

# ---------------- VIEW APPLICATIONS ----------------

if view_btn:

    st.header("Applied Candidates")

    res = r.get(
        f"{be_server_url}/view_all_applications"
    )

    data = res.json()

    if data:

        table_data = []

        count = 1

        for row in data:

            table_data.append({
                "No": count,
                "Email": row["email"],
                "Applied Role": row["job_role"]
            })

            count += 1

        st.dataframe(table_data)

    else:

        st.error("No Applications Found")