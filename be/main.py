from fastapi import FastAPI
from db_connection import supabase_client_object

app = FastAPI()

@app.post("/register")
def register_function(payload: dict):

    if payload["password"] != payload["confirm_password"]:
        return {"msg": "Passwords do not match"}

    supabase_client_object.table("users").insert({
        "name": payload["name"],
        "email": payload["email"],
        "password": payload["password"],
        "role": payload["role"]
    }).execute()

    return {"msg": "User Registered Successfully"}


@app.post("/login")
def login_function(payload: dict):

    response = (
        supabase_client_object
        .table("users")
        .select("*")
        .eq("email", payload["email"])
        .eq("password", payload["password"])
        .eq("role", payload["role"])
        .execute()
    )

    if response.data:

        return {
            "role": response.data[0]["role"]
        }

    return {
        "msg": "Invalid Credentials"
    }


@app.post("/apply_job")
def apply_job(payload: dict):

    supabase_client_object.table(
        "applied_details"
    ).insert({

        "email": payload["email"],
        "job_role": payload["job_role"],
        "status": "Applied"

    }).execute()

    return {
        "msg": "Job Applied Successfully"
    }


@app.get("/view_applied_details/{email}")
def view_applied_details(email: str):

    response = (
        supabase_client_object
        .table("applied_details")
        .select("*")
        .eq("email", email)
        .execute()
    )

    return response.data
@app.get("/view_all_applications")
def view_all_applications():

    response = (
        supabase_client_object
        .table("applied_details")
        .select("*")
        .execute()
    )

    return response.data
@app.post("/post_job")
def post_job(payload: dict):

    supabase_client_object.table(
        "jobs"
    ).insert({

        "role": payload["role"],
        "description": payload["description"],
        "salary": payload["salary"],
        "skills_required": payload["skills_required"],
        "location": payload["location"]

    }).execute()

    return {
        "msg": "Job Posted Successfully"
    }